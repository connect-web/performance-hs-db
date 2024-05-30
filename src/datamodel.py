from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class SkillsRecord:
    attack: int = 0
    defence: int = 0
    strength: int = 0
    hitpoints: int = 0
    ranged: int = 0
    prayer: int = 0
    magic: int = 0
    cooking: int = 0
    woodcutting: int = 0
    fletching: int = 0
    fishing: int = 0
    firemaking: int = 0
    crafting: int = 0
    smithing: int = 0
    mining: int = 0
    herblore: int = 0
    agility: int = 0
    thieving: int = 0
    slayer: int = 0
    farming: int = 0
    runecraft: int = 0
    hunter: int = 0
    construction: int = 0


@dataclass
class ActivitiesRecord:
    league: int = 0
    bounty_hunter_hunter: int = 0
    bounty_hunter_rogue: int = 0
    cs_all: int = 0
    cs_beginner: int = 0
    cs_easy: int = 0
    cs_medium: int = 0
    cs_hard: int = 0
    cs_elite: int = 0
    cs_master: int = 0
    lms_rank: int = 0
    soul_wars_zeal: int = 0
    abyssal_sire: int = 0
    alchemical_hydra: int = 0
    barrows_chests: int = 0
    bryophyta: int = 0
    callisto: int = 0
    cerberus: int = 0
    chambers_of_xeric: int = 0
    chambers_of_xeric_challenge_mode: int = 0
    chaos_elemental: int = 0
    chaos_fanatic: int = 0
    commander_zilyana: int = 0
    corporeal_beast: int = 0
    crazy_archaeologist: int = 0
    dagannoth_prime: int = 0
    dagannoth_rex: int = 0
    dagannoth_supreme: int = 0
    deranged_archaeologist: int = 0
    general_graardor: int = 0
    giant_mole: int = 0
    grotesque_guardians: int = 0
    hespori: int = 0
    kalphite_queen: int = 0
    king_black_dragon: int = 0
    kraken: int = 0
    kreearra: int = 0
    kril_tsutsaroth: int = 0
    mimic: int = 0
    nightmare: int = 0
    nex: int = 0
    phosanis_nightmare: int = 0
    obor: int = 0
    phantom_muspah: int = 0
    sarachnis: int = 0
    scorpia: int = 0
    skotizo: int = 0
    tempoross: int = 0
    the_gauntlet: int = 0
    the_corrupted_gauntlet: int = 0
    theatre_of_blood: int = 0
    theatre_of_blood_hard: int = 0
    thermonuclear_smoke_devil: int = 0
    tombs_of_amascut: int = 0
    tombs_of_amascut_expert: int = 0
    tzkal_zuk: int = 0
    tztok_jad: int = 0
    venenatis: int = 0
    vetion: int = 0
    vorkath: int = 0
    wintertodt: int = 0
    zalcano: int = 0
    zulrah: int = 0
    rifts_closed: int = 0
    artio: int = 0
    calvarion: int = 0
    duke_sucellus: int = 0
    spindel: int = 0
    the_leviathan: int = 0
    the_whisperer: int = 0
    vardorvis: int = 0


@dataclass
class HiscoreRecord:
    scrape_ts: datetime
    scrape_date: date
    player_id: int
    skills: SkillsRecord = SkillsRecord()
    activities: ActivitiesRecord = ActivitiesRecord()
