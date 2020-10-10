# -*- coding: utf-8 -*-
import pandas as pd
import sys
import os
import datetime
import openpyxl

from . import team_data
from . import mk_corr_list
from . import input_tcsv
from . import mylist
from . import mkxl


def calc_corr_number_of_games(filename,save_dir,myteam,n):
	calc_corr(filename,save_dir,myteam,0,n,0,0)
	return
	
def calc_corr_days(filename,save_dir,myteam,datemin,datemax):
	calc_corr(filename,save_dir,myteam,1,0,datemin,datemax)
	return
	
def calc_corr(filename,save_dir,myteam,mode,n,datemin,datemax):
	if not(os.path.exists(save_dir)):
		os.mkdir(save_dir)
	df = input_tcsv.input_tcsv(filename)
	df['elapsedTime']=df['elapsedTime'].astype(int)
	df['win']=df['win'].astype(int)
	df.loc[df['elapsedTime']==0,'elapsedTime']=180
	df_league = df[mylist.league_list].copy()
	df_league = df_league[df_league['gameModeKey']==' league_team']

	df_league.loc[df_league['alpha1Kill']==' ','alpha1Kill']=0
	df_league.loc[df_league['alpha2Kill']==' ','alpha2Kill']=0
	df_league.loc[df_league['alpha3Kill']==' ','alpha3Kill']=0
	df_league.loc[df_league['alpha1Death']==' ','alpha1Death']=0
	df_league.loc[df_league['alpha2Death']==' ','alpha2Death']=0
	df_league.loc[df_league['alpha3Death']==' ','alpha3Death']=0
	df_league.loc[df_league['alpha1PaintPoint']==' ','alpha1PaintPoint']=0
	df_league.loc[df_league['alpha2PaintPoint']==' ','alpha2PaintPoint']=0
	df_league.loc[df_league['alpha3PaintPoint']==' ','alpha3PaintPoint']=0
	df_league.loc[df_league['alpha1Special']==' ','alpha1Special']=0
	df_league.loc[df_league['alpha2Special']==' ','alpha2Special']=0
	df_league.loc[df_league['alpha3Special']==' ','alpha3Special']=0
	
	df_league['alpha1Kill'] = df_league['alpha1Kill'].astype(int)
	df_league['alpha2Kill'] = df_league['alpha2Kill'].astype(int)
	df_league['alpha3Kill'] = df_league['alpha3Kill'].astype(int)
	df_league['alpha1Death'] = df_league['alpha1Death'].astype(int)
	df_league['alpha2Death'] = df_league['alpha2Death'].astype(int)
	df_league['alpha3Death'] = df_league['alpha3Death'].astype(int)
	
	df_league['alpha1KillPerDeath'] = df_league['alpha1Kill'].astype(int)
	df_league['alpha2KillPerDeath'] = df_league['alpha2Kill'].astype(int)
	df_league['alpha3KillPerDeath'] = df_league['alpha3Kill'].astype(int)
	df_league.loc[df_league['alpha1Death']>0,'alpha1KillPerDeath']=df_league['alpha1Kill'].astype(int)/df_league['alpha1Death'].astype(int)
	df_league.loc[df_league['alpha2Death']>0,'alpha2KillPerDeath']=df_league['alpha2Kill'].astype(int)/df_league['alpha2Death'].astype(int)
	df_league.loc[df_league['alpha3Death']>0,'alpha3KillPerDeath']=df_league['alpha3Kill'].astype(int)/df_league['alpha3Death'].astype(int)

	df_league['alpha1Kill'] = df_league['alpha1Kill'].astype(int)
	df_league['alpha2Kill'] = df_league['alpha2Kill'].astype(int)
	df_league['alpha3Kill'] = df_league['alpha3Kill'].astype(int)

	df_league['alpha1Death'] = df_league['alpha1Death'].astype(int)
	df_league['alpha2Death'] = df_league['alpha2Death'].astype(int)
	df_league['alpha3Death'] = df_league['alpha3Death'].astype(int)

	df_league['alpha1PaintPointPerMin'] = df_league['alpha1PaintPoint'].astype(int)/df['elapsedTime']*60
	df_league['alpha2PaintPointPerMin'] = df_league['alpha2PaintPoint'].astype(int)/df['elapsedTime']*60
	df_league['alpha3PaintPointPerMin'] = df_league['alpha3PaintPoint'].astype(int)/df['elapsedTime']*60
	df_league['alpha1SpecialPerMin'] = df_league['alpha1Special'].astype(int)/df['elapsedTime']*60
	df_league['alpha2SpecialPerMin'] = df_league['alpha2Special'].astype(int)/df['elapsedTime']*60
	df_league['alpha3SpecialPerMin'] = df_league['alpha3Special'].astype(int)/df['elapsedTime']*60


	df_league_out = df_league[mylist.league_out_list].copy()
	df_league_out['elapsedTime'] = df['elapsedTime']
	df_league_out[myteam.player.usname+'_Kill'] = df['playerKill'].astype(int)
	df_league_out[myteam.player.usname+'_Death'] = df['playerDeath'].astype(int)
	df_league_out[myteam.player.usname+'_KillPerMin'] = df_league_out[myteam.player.usname+'_Kill']/df['elapsedTime']*60
	df_league_out[myteam.player.usname+'_DeathPerMin'] = df_league_out[myteam.player.usname+'_Death']/df['elapsedTime']*60
	df_league_out[myteam.player.usname+'_KillPerDeath'] = df['playerKill'].astype(int)/df['playerDeath'].astype(int)
	df_league_out[myteam.player.usname+'_PaintPoint'] = df['playerPaintPoint'].astype(int)
	df_league_out[myteam.player.usname+'_Special'] = df['playerSpecial'].astype(int)
	df_league_out[myteam.player.usname+'_WeaponID'] = df['playerWeaponID'].astype(int)
	df_league_out[myteam.player.usname+'_PaintPointPerMin'] = df['playerPaintPoint'].astype(int)/df['elapsedTime'].astype(int)*60
	df_league_out[myteam.player.usname+'_SpecialPerMin'] = df['playerSpecial'].astype(int)/df['elapsedTime'].astype(int)*60
	
	df_league_out[myteam.friend1.usname+'_Kill'] = 0
	df_league_out[myteam.friend1.usname+'_Death'] = 0
	df_league_out[myteam.friend1.usname+'_KillPerDeath'] = 0
	df_league_out[myteam.friend1.usname+'_PaintPoint'] = 0
	df_league_out[myteam.friend1.usname+'_Special'] = 0
	df_league_out[myteam.friend1.usname+'_WeaponID'] = 0
	df_league_out[myteam.friend1.usname+'_SpecialPerMin'] = 0
	df_league_out[myteam.friend1.usname+'_PaintPointPerMin'] = 0
	
	df_league_out[myteam.friend2.usname+'_Kill'] = 0
	df_league_out[myteam.friend2.usname+'_Death'] = 0
	df_league_out[myteam.friend2.usname+'_KillPerDeath'] = 0
	df_league_out[myteam.friend2.usname+'_PaintPoint'] = 0
	df_league_out[myteam.friend2.usname+'_Special'] = 0
	df_league_out[myteam.friend2.usname+'_WeaponID'] = 0
	df_league_out[myteam.friend2.usname+'_PaintPointPerMin'] = 0
	df_league_out[myteam.friend2.usname+'_SpecialPerMin'] = 0
	
	df_league_out[myteam.friend3.usname+'_Kill'] = 0
	df_league_out[myteam.friend3.usname+'_Death'] = 0
	df_league_out[myteam.friend3.usname+'_KillPerDeath'] = 0
	df_league_out[myteam.friend3.usname+'_PaintPoint'] = 0
	df_league_out[myteam.friend3.usname+'_Special'] = 0
	df_league_out[myteam.friend3.usname+'_WeaponID'] = 0
	df_league_out[myteam.friend3.usname+'_PaintPointPerMin'] = 0
	df_league_out[myteam.friend3.usname+'_SpecialPerMin'] = 0

	df_league_out[myteam.player.usname] = 1
	df_league_out[myteam.friend1.usname] = 0
	df_league_out[myteam.friend2.usname] = 0
	df_league_out[myteam.friend3.usname] = 0

	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname]=1
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname]=1
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname]=1
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname]=1
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname]=1
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname]=1
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname]=1
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname]=1
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname]=1
	df_league_out['myteam'] = df_league_out[myteam.friend1.usname]*df_league_out[myteam.friend2.usname]*df_league_out[myteam.friend3.usname]
	df_league_out = df_league_out[df_league_out['myteam']==1]

	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_Kill']=df_league['alpha1Kill']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_Kill']=df_league['alpha1Kill']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_Kill']=df_league['alpha1Kill']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_Kill']=df_league['alpha2Kill']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_Kill']=df_league['alpha2Kill']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_Kill']=df_league['alpha2Kill']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_Kill']=df_league['alpha3Kill']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_Kill']=df_league['alpha3Kill']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_Kill']=df_league['alpha3Kill']

	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_Death']=df_league['alpha1Death']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_Death']=df_league['alpha1Death']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_Death']=df_league['alpha1Death']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_Death']=df_league['alpha2Death']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_Death']=df_league['alpha2Death']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_Death']=df_league['alpha2Death']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_Death']=df_league['alpha3Death']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_Death']=df_league['alpha3Death']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_Death']=df_league['alpha3Death']

	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_KillPerDeath']=df_league['alpha1KillPerDeath']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_KillPerDeath']=df_league['alpha1KillPerDeath']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_KillPerDeath']=df_league['alpha1KillPerDeath']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_KillPerDeath']=df_league['alpha2KillPerDeath']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_KillPerDeath']=df_league['alpha2KillPerDeath']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_KillPerDeath']=df_league['alpha2KillPerDeath']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_KillPerDeath']=df_league['alpha3KillPerDeath']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_KillPerDeath']=df_league['alpha3KillPerDeath']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_KillPerDeath']=df_league['alpha3KillPerDeath']

	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_PaintPoint']=df_league['alpha1PaintPoint']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_PaintPoint']=df_league['alpha1PaintPoint']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_PaintPoint']=df_league['alpha1PaintPoint']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_PaintPoint']=df_league['alpha2PaintPoint']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_PaintPoint']=df_league['alpha2PaintPoint']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_PaintPoint']=df_league['alpha2PaintPoint']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_PaintPoint']=df_league['alpha3PaintPoint']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_PaintPoint']=df_league['alpha3PaintPoint']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_PaintPoint']=df_league['alpha3PaintPoint']

	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_Special']=df_league['alpha1Special']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_Special']=df_league['alpha1Special']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_Special']=df_league['alpha1Special']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_Special']=df_league['alpha2Special']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_Special']=df_league['alpha2Special']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_Special']=df_league['alpha2Special']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_Special']=df_league['alpha3Special']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_Special']=df_league['alpha3Special']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_Special']=df_league['alpha3Special']

	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_WeaponID']=df_league['alpha1WeaponID']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_WeaponID']=df_league['alpha1WeaponID']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_WeaponID']=df_league['alpha1WeaponID']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_WeaponID']=df_league['alpha2WeaponID']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_WeaponID']=df_league['alpha2WeaponID']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_WeaponID']=df_league['alpha2WeaponID']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_WeaponID']=df_league['alpha3WeaponID']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_WeaponID']=df_league['alpha3WeaponID']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_WeaponID']=df_league['alpha3WeaponID']

	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_PaintPointPerMin']=df_league['alpha1PaintPointPerMin']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_PaintPointPerMin']=df_league['alpha1PaintPointPerMin']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_PaintPointPerMin']=df_league['alpha1PaintPointPerMin']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_PaintPointPerMin']=df_league['alpha2PaintPointPerMin']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_PaintPointPerMin']=df_league['alpha2PaintPointPerMin']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_PaintPointPerMin']=df_league['alpha2PaintPointPerMin']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_PaintPointPerMin']=df_league['alpha3PaintPointPerMin']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_PaintPointPerMin']=df_league['alpha3PaintPointPerMin']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_PaintPointPerMin']=df_league['alpha3PaintPointPerMin']

	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_SpecialPerMin']=df_league['alpha1SpecialPerMin']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_SpecialPerMin']=df_league['alpha1SpecialPerMin']
	df_league_out.loc[df_league_out['alpha1PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_SpecialPerMin']=df_league['alpha1SpecialPerMin']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_SpecialPerMin']=df_league['alpha2SpecialPerMin']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_SpecialPerMin']=df_league['alpha2SpecialPerMin']
	df_league_out.loc[df_league_out['alpha2PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_SpecialPerMin']=df_league['alpha2SpecialPerMin']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend1.pid,myteam.friend1.usname+'_SpecialPerMin']=df_league['alpha3SpecialPerMin']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend2.pid,myteam.friend2.usname+'_SpecialPerMin']=df_league['alpha3SpecialPerMin']
	df_league_out.loc[df_league_out['alpha3PrincipalID']==' '+myteam.friend3.pid,myteam.friend3.usname+'_SpecialPerMin']=df_league['alpha3SpecialPerMin']

	df_league_out[myteam.friend1.usname+'_KillPerMin'] = df_league_out[myteam.friend1.usname+'_Kill']/df['elapsedTime'].astype(int)*60
	df_league_out[myteam.friend1.usname+'_DeathPerMin'] = df_league_out[myteam.friend1.usname+'_Death']/df['elapsedTime'].astype(int)*60
	df_league_out[myteam.friend2.usname+'_KillPerMin'] = df_league_out[myteam.friend2.usname+'_Kill']/df['elapsedTime'].astype(int)*60
	df_league_out[myteam.friend2.usname+'_DeathPerMin'] = df_league_out[myteam.friend2.usname+'_Death']/df['elapsedTime'].astype(int)*60
	df_league_out[myteam.friend3.usname+'_KillPerMin'] = df_league_out[myteam.friend3.usname+'_Kill']/df['elapsedTime'].astype(int)*60
	df_league_out[myteam.friend3.usname+'_DeathPerMin'] = df_league_out[myteam.friend3.usname+'_Death']/df['elapsedTime'].astype(int)*60


	df_league_out = df_league_out.drop("alpha1PrincipalID", axis=1)
	df_league_out = df_league_out.drop("alpha2PrincipalID", axis=1)
	df_league_out = df_league_out.drop("alpha3PrincipalID", axis=1)
	
	df_league_out.loc[df_league_out['bravo1udemaeName']=='','bravo1udemaeName']=0
	df_league_out.loc[df_league_out['bravo2udemaeName']=='','bravo2udemaeName']=0
	df_league_out.loc[df_league_out['bravo3udemaeName']=='','bravo3udemaeName']=0
	df_league_out.loc[df_league_out['bravo4udemaeName']=='','bravo4udemaeName']=0
	df_league_out.loc[df_league_out['bravo1udemaeName']==' ','bravo1udemaeName']=0
	df_league_out.loc[df_league_out['bravo2udemaeName']==' ','bravo2udemaeName']=0
	df_league_out.loc[df_league_out['bravo3udemaeName']==' ','bravo3udemaeName']=0
	df_league_out.loc[df_league_out['bravo4udemaeName']==' ','bravo4udemaeName']=0
	df_league_out.loc[pd.isnull(df_league_out['bravo1udemaeName']),'bravo1udemaeName']=0
	df_league_out.loc[pd.isnull(df_league_out['bravo2udemaeName']),'bravo2udemaeName']=0
	df_league_out.loc[pd.isnull(df_league_out['bravo3udemaeName']),'bravo3udemaeName']=0
	df_league_out.loc[pd.isnull(df_league_out['bravo4udemaeName']),'bravo4udemaeName']=0
	df_league_out = df_league_out.replace(' C-',1)
	df_league_out = df_league_out.replace(' C',2)
	df_league_out = df_league_out.replace(' C+',3)
	df_league_out = df_league_out.replace(' B-',4)
	df_league_out = df_league_out.replace(' B',5)
	df_league_out = df_league_out.replace(' B+',6)
	df_league_out = df_league_out.replace(' A-',7)
	df_league_out = df_league_out.replace(' A',8)
	df_league_out = df_league_out.replace(' A+',9)
	df_league_out = df_league_out.replace(' S',10)
	df_league_out = df_league_out.replace(' S+',11)
	df_league_out = df_league_out.replace(' X',12)
	df_league_out['bravo1udemaeName'] = df_league_out['bravo1udemaeName'].astype(int)
	df_league_out['bravo2udemaeName'] = df_league_out['bravo2udemaeName'].astype(int)
	df_league_out['bravo3udemaeName'] = df_league_out['bravo3udemaeName'].astype(int)
	df_league_out['bravo4udemaeName'] = df_league_out['bravo4udemaeName'].astype(int)
	df_league_out['enemy_udemae_average'] = (df_league_out['bravo1udemaeName']+df_league_out['bravo2udemaeName']+df_league_out['bravo3udemaeName']+df_league_out['bravo4udemaeName'])/4
	df_league_out['datetime'] = pd.to_datetime(df_league_out['startTime'], format=" %Y/%m/%d %H:%M:%S")
	df_league_out['date'] = df_league_out['datetime'].dt.strftime('%Y%m%d')
		
	corr_list = mk_corr_list.mk_corr_list(myteam)
	df_league_tower = df_league_out[df_league_out['gameRuleKey']==' tower_control'] #ヤグラ
	df_league_zones = df_league_out[df_league_out['gameRuleKey']==' splat_zones'] #エリア
	df_league_clam = df_league_out[df_league_out['gameRuleKey']==' clam_blitz'] #アサリ
	df_league_hoko = df_league_out[df_league_out['gameRuleKey']==' rainmaker'] #ホコ

	if mode==0:
		df_league_tower = df_league_tower.head(n)
		df_league_zones = df_league_zones.head(n)
		df_league_clam = df_league_clam.head(n)
		df_league_hoko = df_league_hoko.head(n)
	if mode==1:
		daterange_min = datetime.datetime.strptime(datemin, "%Y%m%d")
		daterange_max = datetime.datetime.strptime(datemax, "%Y%m%d")
		daterange_max = daterange_max + datetime.timedelta(days=1)
		df_league_tower = df_league_tower[df_league_tower['datetime']>=daterange_min]
		df_league_tower = df_league_tower[df_league_tower['datetime']<=daterange_max]	
		df_league_zones = df_league_zones[df_league_zones['datetime']>=daterange_min]
		df_league_zones = df_league_zones[df_league_zones['datetime']<=daterange_max]	
		df_league_clam = df_league_clam[df_league_clam['datetime']>=daterange_min]
		df_league_clam = df_league_clam[df_league_clam['datetime']<=daterange_max]	
		df_league_hoko = df_league_hoko[df_league_hoko['datetime']>=daterange_min]
		df_league_hoko = df_league_hoko[df_league_hoko['datetime']<=daterange_max]	




	df_league_tower_corr = df_league_tower[corr_list].copy()
	df_league_zones_corr = df_league_zones[corr_list].copy()
	df_league_clam_corr = df_league_clam[corr_list].copy()
	df_league_hoko_corr = df_league_hoko[corr_list].copy()


	mkxl.outxlsx(df_league_out,save_dir,'league_all')
	mkxl.outxlsx(df_league_tower_corr.corr(),save_dir,'tower_control_corr')
	mkxl.outxlsx(df_league_zones_corr.corr(),save_dir,'splat_zones_corr')
	mkxl.outxlsx(df_league_clam_corr.corr(),save_dir,'clam_blitz_corr')
	mkxl.outxlsx(df_league_hoko_corr.corr(),save_dir,'rainmaker_corr')
	gameslist = [len(df_league_zones_corr),len(df_league_tower_corr),len(df_league_hoko_corr),len(df_league_clam_corr)]
	mkxl.outcorr(save_dir,gameslist,myteam)
	return