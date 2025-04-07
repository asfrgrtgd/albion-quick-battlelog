import requests

def main():
  battle_id = input("Enter Battle ID (e.g., 44928871): ").strip()
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
  print("===== Aggregated Results =====")
  for guild_name, info in guild_data.items():
    print(f"Guild: {guild_name}")
    print(f"  Kills: {info['kills']}")
    print(f"  Deaths: {info['deaths']}")
    print(f"  Members: {len(info['members'])}")
    print(f"  Member List: {','.join(info['members'])}")
    print("-" * 40)

if __name__ == "__main__":
  main()
