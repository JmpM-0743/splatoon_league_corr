# -*- coding: utf-8 -*-

from context import splatoon_league_corr

import unittest


class BasicTestSuite(unittest.TestCase):
	"""calc_corr_number_of_games sample cases."""
	player = splatoon_league_corr.ika_data('xxxx','自分','plater')
	friend1 = splatoon_league_corr.ika_data('xxxx','フレンド１','friend1')
	friend2 = splatoon_league_corr.ika_data('xxxx','フレンド２','friend2')
	friend3 = splatoon_league_corr.ika_data('xxxx','フレンド３','friend3')
	myteam = splatoon_league_corr.team_data(player,friend1,friend2,friend3)
	splatoon_league_corr.calc_corr_number_of_games('ikaWidgetCSV_xxx.tcsv','output',myteam,50)
	
	def test_absolute_truth_and_meaning(self):
		assert True


if __name__ == '__main__':
	unittest.main()