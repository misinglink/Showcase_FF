ss_data_cols = """Name
Team
Opponent
Position
Projection
Actual
Price
Value
proj_own
dk_point
dk_25_percentile
dk_50_percentile
dk_75_percentile
dk_85_percentile
dk_95_percentile
dk_99_percentile
fd_points
fd_25_percentile
fd_50_percentile
fd_75_percentile
fd_85_percentile
fd_95_percentile
fd_99_percentile
fdraft_points
fdraft_25_percentile
fdraft_50_percentile
fdraft_75_percentile
fdraft_85_percentile
fdraft_95_percentile
fdraft_99_percentile
yahoo_points
yahoo_25_percentile
yahoo_50_percentile
yahoo_75_percentile
yahoo_85_percentile
yahoo_95_percentile
yahoo_99_percentile
dk_std
fd_std
fdraft_std
yahoo_std
pass_attempts
completions
passing_yards
passing_td
receptions
receiving_yards
receiving_td
rushes
rushing_yards
rushing_td""".split('\n')

_4f4_proj_cols = """Season
Week
PID
Player
Pos
Team
Opp
aFPA
aFPA_Rk
FFPts
Comp
Pass_Att
Pass_Yds
Pass_TD
INT
Rush_Att
Rush_Yds
Rush_TD
Rec
Rec_Yds
Rec_TD
Pa1D
Ru1D
Rec1D
Fum
XP
FG
Grade""".split('\n')

_4f4_ceil_cols = """Season
Week
PID
Player
Pos
Team
Opp
aFPA
aFPA_Rk
FFPts
Comp
Pass_Att
Pass_Yds
Pass_TD
INT
Rush_Att
Rush_Yds
Rush_TD
Rec
Rec_Yds
Rec_TD
Pa1D
Ru1D
Rec1D
Fum
XP
FG
Grade
DK_Proj
DK_Price
DK_Val
DK_Pts_per_1k
DK_Flr
DK_Flr_Val
DK_Flr_per_1k
DK_Ceil
DK_Ceil_Val
DK_Ceil_per_1k
DK_Wk_Change
DK_Own_Percent
FD_Proj
FD_Price
FD_Val
FD_Pts_pr_1k
FD_Flr
FD_Flr_Val
FD_Flr_pr_1k
FD_Ceil
FD_Ceil_Val
FD_Ceil_pr_1k
FD_Wk_Change
FD_Own_Percent
Y_Proj
Y_Price
Y_Val
Y_Pt_pr_Dollar
Y_Flr
Y_Flr_Val
Y_Flr_pr_Dollar
Y_Ceil
Y_Ceil_Val
Y_Ceil_pr_Dollar
Y_Wk_Change
FyD_Proj
FyD_Price
FyD_Val
FyD_Pt_pr_1k
FyD_Flr
FyD_Flr_Val
FyD_Flr_pr_1k
FyD_Ceil
FyD_Ceil_Val
FyD_Ceil_pr_1k
FyD_Wk_Change
O_U
Line
Team_O_U""".split('\n')

_4f4_wrcb_cols = ['Player', 'Team', 'Opponent', 'Matchup', 'Shadow']
_4f4_wr_fp_cols = ['Player', 'Pos', 'Team', 'G', 'W5', 'W6', 'W7', 'W8', 'DK_Pts','DK_Pts_pr_G']
_4f4_rb_fp_cols = ['Player', 'Pos', 'Team', 'G', 'W13', 'W14', 'W15', 'DK_Pts','DK_Pts_pr_G']
_4f4_rb_tar_cols = ['Player', 'Pos', 'Team', 'G', 'W13', 'W14', 'W15', 'TGTs', 'TGTs_pr_G', 'Array']
airy_wr_cols = ['full_name', 'position', 'team', 'targets', 'rec', 'rec_yards',
           'air_yards', 'yac', 'td', 'adot', 'racr', 'ms_air', 'tgt_share', 'wopr',
           'ppr', 'Tar_pr_Gam', 'AY_pr_Gam']
airy_te_cols = ['full_name', 'position', 'team', 'targets', 'rec', 'rec_yards',
           'air_yards', 'yac', 'td', 'adot', 'racr', 'ms_air', 'tgt_share', 'wopr',
           'ppr', 'Tar_pr_3']

_4f4_redZ_cols = ['Season', 'Week', 'PID', 'Player', 'Pos', 'Team', 'Opp', 'aFPA',
'aFPA_Rk', 'FFPts', 'Comp', 'Pass_Att', 'Pass_Yds', 'Pass_TD', 'INT',
'Rush_Att', 'Rush_Yds', 'Rush_TD', 'Rec', 'Rec_Yds', 'Rec_TD', 'Pa1D',
'Ru1D', 'Rec1D', 'Fum', 'XP', 'FG', 'Grade', 'DK_proj', 'DK_price',
'DK_val', 'DK_Pt_pr_1k', 'DK_Flr', 'DK_Flr_Val', 'DK_Flr_pr_1k',
'DK_Ceil', 'DK_Ceil_Val', 'DK_Ceil_pr_1k', 'DK_Wk_Change',
'DK_Own_Percent', 'FD_proj', 'FD_price', 'FD_val', 'FD_Pt_pr_1k',
'FD_Flr', 'FD_Flr_Val', 'FD_Flr_pr_1k', 'FD_Ceil',
'FD_Ceil_Val', 'FD_Ceil_pr_1k', 'FD_Wk_Change', 'FD_Own_Percent',
'Y_proj', 'Y_price', 'Y_val', 'Y_Pt_pr_DOllar', 'Y_Flr',
'Y_Flr_Val', 'Y_Flr_pr_Dollar', 'Y_Ceil', 'Y_Ceil_Val',
'Y_Ceil_pr_Dollar', 'Y_Wk_Change', 'FyD_proj', 'FyD_price', 'FyD_val',
'FyD_Pt_pr_1k', 'FyD_Flr', 'FyD_Flr_Val', 'FyD_Flr_pr_1k',
'FyD_Ceil', 'FyD_Ceil_Val', 'FyD_Ceil_pr_1k', 'FyD_Wk_Change',
'O_U', 'Line', 'Team_O_U']

etr_ceiling_cols = ['Season', 'Week', 'PID', 'Player', 'Pos', 'Team', 'Opp', 'aFPA',
'aFPA_Rk', 'FFPts', 'Comp', 'Pass_Att', 'Pass_Yds', 'Pass_TD', 'INT',
'Rush_Att', 'Rush_Yds', 'Rush_TD', 'Rec', 'Rec_Yds', 'Rec_TD', 'Pa1D',
'Ru1D', 'Rec1D', 'Fum', 'XP', 'FG', 'Grade', 'DK_proj', 'DK_price',
'DK_val', 'DK_Pt_pr_1k', 'DK_Flr', 'DK_Flr_Val', 'DK_Flr_pr_1k',
'DK_Ceil', 'DK_Ceil_Val', 'DK_Ceil_pr_1k', 'DK_Wk_Change',
'DK_Own_Percent', 'FD_proj', 'FD_price', 'FD_val', 'FD_Pt_pr_1k',
'FD_Flr', 'FD_Flr_Val', 'FD_Flr_pr_1k', 'FD_Ceil',
'FD_Ceil_Val', 'FD_Ceil_pr_1k', 'FD_Wk_Change', 'FD_Own_Percent',
'Y_proj', 'Y_price', 'Y_val', 'Y_Pt_pr_Dollar', 'Y_Flr',
'Y_Flr_Val', 'Y_Flr_pr_Dollar', 'Y_Ceil', 'Y_Ceil_Val',
'Y_Ceil_pr_Dollar', 'Y_Wk_Change', 'FyD_proj', 'FyD_price', 'FyD_val',
'FyD_Pt_pr_1k', 'FyD_Flr', 'FyD_Flr_Val', 'FyD_Flr_pr_1k',
'FyD_Ceil', 'FyD_Ceil_Val', 'FyD_Ceil_pr_1k', 'FyD_Wk_Change',
'O_U', 'Line', 'Team_O_U']