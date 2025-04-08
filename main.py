import requests
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

def process_battle(battle_id):
  limit = 51
  offset = 0
  guild_data = {}
  while True:
    url = f"https://gameinfo-ams.albiononline.com/api/gameinfo/events/battle/{battle_id}?offset={offset}&limit={limit}"
    response = requests.get(url)
    if response.status_code != 200:
      print(f"Failed to retrieve data. Status code: {response.status_code}")
      break
    events = response.json()
    if not events:
      break
    for event in events:
      killer_info = event.get("Killer", {})
      killer_guild_name = killer_info.get("GuildName") or "NoGuild"
      killer_player_name = killer_info.get("Name", "UnknownPlayer")
      if killer_guild_name not in guild_data:
        guild_data[killer_guild_name] = {
          "members": set(),
          "kills": 0,
          "deaths": 0
        }
      guild_data[killer_guild_name]["members"].add(killer_player_name)
      guild_data[killer_guild_name]["kills"] += 1
      victim_info = event.get("Victim", {})
      victim_guild_name = victim_info.get("GuildName") or "NoGuild"
      victim_player_name = victim_info.get("Name", "UnknownPlayer")
      if victim_guild_name not in guild_data:
        guild_data[victim_guild_name] = {
          "members": set(),
          "kills": 0,
          "deaths": 0
        }
      guild_data[victim_guild_name]["members"].add(victim_player_name)
      guild_data[victim_guild_name]["deaths"] += 1
      participants = event.get("Participants", [])
      for part in participants:
        p_guild_name = part.get("GuildName") or "NoGuild"
        p_player_name = part.get("Name", "UnknownPlayer")
        if p_guild_name not in guild_data:
          guild_data[p_guild_name] = {
            "members": set(),
            "kills": 0,
            "deaths": 0
          }
        guild_data[p_guild_name]["members"].add(p_player_name)
      group_members = event.get("GroupMembers", [])
      for gm in group_members:
        gm_guild_name = gm.get("GuildName") or "NoGuild"
        gm_player_name = gm.get("Name", "UnknownPlayer")
        if gm_guild_name not in guild_data:
          guild_data[gm_guild_name] = {
            "members": set(),
            "kills": 0,
            "deaths": 0
          }
        guild_data[gm_guild_name]["members"].add(gm_player_name)
    offset += limit
  return guild_data

def process_multiple_battles(battle_ids):
  combined_data = {}
  
  for battle_id in battle_ids:
    battle_id = battle_id.strip()
    if not battle_id:
      continue
      
    print(f"Processing battle ID: {battle_id}")
    battle_data = process_battle(battle_id)
    
    # Merge battle data into combined data
    for guild_name, info in battle_data.items():
      if guild_name not in combined_data:
        combined_data[guild_name] = {
          "members": set(),
          "kills": 0,
          "deaths": 0
        }
      combined_data[guild_name]["kills"] += info["kills"]
      combined_data[guild_name]["deaths"] += info["deaths"]
      combined_data[guild_name]["members"].update(info["members"])
  
  return combined_data

def display_results(guild_data, is_combined=False):
  if is_combined:
    print(f"\n{Back.BLUE}{Fore.WHITE}{Style.BRIGHT}===== Combined Results from Multiple Battles ====={Style.RESET_ALL}")
  else:
    print(f"\n{Back.BLUE}{Fore.WHITE}{Style.BRIGHT}===== Battle Results ====={Style.RESET_ALL}")
  
  print("\n" + "=" * 60)
  
  # Sort guilds by kills in descending order
  sorted_guilds = sorted(guild_data.items(), key=lambda x: x[1]['kills'], reverse=True)
  
  for guild_name, info in sorted_guilds:
    # Calculate kill/death ratio
    kd_ratio = info['kills'] / info['deaths'] if info['deaths'] > 0 else info['kills'] if info['kills'] > 0 else 0
    
    # Guild header with color based on kills vs deaths
    if info['kills'] > info['deaths']:
      guild_color = Fore.GREEN
    elif info['kills'] < info['deaths']:
      guild_color = Fore.RED
    else:
      guild_color = Fore.YELLOW
    
    print(f"{guild_color}{Style.BRIGHT}Guild: {guild_name}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}├─ {Fore.GREEN}Kills: {info['kills']}")
    print(f"{Fore.CYAN}├─ {Fore.RED}Deaths: {info['deaths']}")
    print(f"{Fore.CYAN}├─ {Fore.YELLOW}K/D Ratio: {kd_ratio:.2f}")
    print(f"{Fore.CYAN}├─ {Fore.BLUE}Members: {len(info['members'])}")
    print(f"{Fore.CYAN}└─ {Fore.MAGENTA}Member List: {Fore.WHITE}{','.join(sorted(info['members']))}")
    print("-" * 60)

def main():
  while True:
    battle_id_input = input("Enter Battle ID(s) (space-separated for multiple battles): ").strip()
    battle_ids = battle_id_input.split()
    
    if not battle_ids:
      print("No battle IDs provided.")
      continue
    
    if len(battle_ids) == 1:
      # Process single battle
      guild_data = process_battle(battle_ids[0])
      display_results(guild_data)
    else:
      # Process multiple battles
      guild_data = process_multiple_battles(battle_ids)
      display_results(guild_data, is_combined=True)
    
    continue_choice = input("Would you like to check another battle? (yes/no): ").strip().lower()
    if continue_choice not in ['yes', 'y']:
      print("Thank you for using Albion Quick Battlelog. Goodbye!")
      break

if __name__ == "__main__":
  main()
