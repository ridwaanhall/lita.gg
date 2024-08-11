class PlayerInSkill:
    '''
    List of Players in Skill shorted by Audit Time
    '''
    def __init__(self, 
                 gender: int = 0, 
                 skillId: int = 1, 
                 page: int = 1, 
                 levelIds: list[int] = '', 
                 newBie: int = 0,
                 order: str = '',
                 positionIds: list[int] = '', 
                 rows: int = 50,
                 sort: str = ''):
        '''
        List of Players in Skill
        gender: 
            0 = both, 1 = male, 2 = female
        skillId: 
            1 = Mobile Legends, 20 = Teman Curhat, 3 = PUBG, 2 = Free Fire, 100 = Ludo King, 
            139 = Eggy Party, 90 = Stumble Guys, 22 = Magic Chess, 21 = Valorant, 18 = COD: Mobile, 
            69 = Genshin Impact, 23 = Sausage Man, 87 = AoV, 10 = LOL: Wild Rift, 65 = Dota 2, 
            89 = Point Blank, 60 = CS2, 102 =  Black Desert Mobile, 103 = Sky : Children of the light, 
            109 = Supersus, 113 = Let's Get Rich, 122 = Teman Nyanyi
        page:
            1 to end
        levelIds:

        newBie (default = 0):   
            0 = false, 1 = true
        order:
            None = 
            desc = descending (default:lastest)
            asc = ascending (oldest)
        positionIds:

        rows:
            1 to 50
        sort:
            None = Recomendation
            auditTime = sort by audit time
            avgStar = sort by avg star
            price = sort by price
        '''
        self.gender = gender
        self.skillId = skillId
        self.page = page
        self.levelIds = levelIds
        self.newBie = newBie
        self.order = order
        self.positionIds = positionIds
        self.rows = rows
        self.sort = sort

    def player_inskill_func(self):
        '''
        player inskill - list of players
        '''
        params_player_inskill = {
            "gender": self.gender,
            "levelIds": self.levelIds,
            "newBie": self.newBie,
            "order": self.order,
            "page": self.page,
            "positionIds": self.positionIds,
            "rows": self.rows,
            "skillId": self.skillId,
            "sort": self.sort
        }
        
        player_inskill = "player/inskill/batch?"  # endpoint
        player_inskill += "&".join([f"{key}={value}" for key, value in params_player_inskill.items()])
        
        return player_inskill


class PlayerDetail:
    '''
    player detail
    '''
    def __init__(self, no):
        self.no = no
    
    def player_detail_func(self):
        '''
        player detail by no
        '''
        params_player_detail = {
            "no": self.no
        }
        
        player_detail = "player/detail/g3?"
        player_detail += "&".join([f"{key}={value}" for key, value in params_player_detail.items()])
        
        return player_detail


class PlayerSkillComment:
    '''
    player skill comment
    '''
    def __init__(self, skillId, userId, page):
        '''
        player skill comment by SkillId and userId
        '''
        self.skillId = skillId
        self.userId = userId
        self.page = page
        self.rows = 50
        
    def player_skill_comment_func(self):
        '''
        player skill comment
        '''
        params_player_skill_comment = {
            "skillId": self.skillId,
            "userId": self.userId,
            "page": self.page,
            "rows": self.rows
        }
        
        player_skill_comment = "player/skill/comment?"
        player_skill_comment += "&".join([f"{key}={value}" for key, value in params_player_skill_comment.items()])
        
        return player_skill_comment
    
    
class PlayerReceived:
    '''
    Handles player-related operations such as gifts, ranks, and orders.
    '''
    def __init__(self, id):
        '''
        Initializes the player with the given id.
        
        Handles player-related operations such as gifts, ranks, and orders.
        '''
        self.id = id
        
    def _construct_url(self, endpoint):
        '''
        Constructs a URL with parameters for the given endpoint.
        '''
        params = {
            "id": self.id
        }
        url = f"player/received/{endpoint}?" + "&".join([f"{key}={value}" for key, value in params.items()])
        return url
    
    def player_received_gift_func(self):
        '''
        Returns the URL for player's received gifts.
        '''
        return self._construct_url("gift")
    
    def player_received_rank_total_func(self):
        '''
        Returns the URL for player's received total rank.
        '''
        return self._construct_url("rank/total")
    
    def player_received_rank_gift_func(self):
        '''
        Returns the URL for player's received rank gifts.
        '''
        return self._construct_url("rank/gift")
    
    def player_received_rank_order_func(self):
        '''
        Returns the URL for player's received rank orders.
        '''
        return self._construct_url("rank/order")


class MomentUserList:
    '''
    moment User List
    '''
    def __init__(self, authorId):
        '''
        Initializes the player with the given id.
        authorId = id.
        '''
        self.authorId = authorId
        self.momentId = 0
        
    def moment_user_list_func(self):
        '''
        moment User List
        '''
        params_moment_user_list = {
            "authorId": self.authorId,
            "momentId": self.momentId
        }
        
        moment_user_list = "moment/user/list?"
        moment_user_list += "&".join([f"{key}={value}" for key, value in params_moment_user_list.items()])
        
        return moment_user_list


class Skills:
    '''
    Skill List
    '''
    def skills_func():
        skill = "skill/"
        return skill