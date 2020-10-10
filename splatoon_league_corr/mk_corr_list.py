
from . import team_data

def mk_corr_list(myteam):
	league_corr_list = [
	 'win'
	,'enemy_udemae_average'	 
	,myteam.player.usname+'_KillPerMin'
	,myteam.player.usname+'_DeathPerMin'
	,myteam.player.usname+'_PaintPointPerMin'
	,myteam.player.usname+'_SpecialPerMin'
	,myteam.friend1.usname+'_KillPerMin'
	,myteam.friend1.usname+'_DeathPerMin'
	,myteam.friend1.usname+'_PaintPointPerMin'	
	,myteam.friend1.usname+'_SpecialPerMin'
	,myteam.friend2.usname+'_KillPerMin'
	,myteam.friend2.usname+'_DeathPerMin'
	,myteam.friend2.usname+'_PaintPointPerMin'
	,myteam.friend2.usname+'_SpecialPerMin'		
	,myteam.friend3.usname+'_KillPerMin'
	,myteam.friend3.usname+'_DeathPerMin'
	,myteam.friend3.usname+'_PaintPointPerMin'
	,myteam.friend3.usname+'_SpecialPerMin'
	]
	return league_corr_list