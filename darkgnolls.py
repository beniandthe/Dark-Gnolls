# Dark Gnolls - We have a "Hero" Class who can be 2 different classes, Warrior, Sorcerer, Rogue. 
#There are 2 basic stats, Strength, Int. Level ups happen every enemy killed and the player fully heals and stats should increase. 
#We have our main enemy "Gnolls" who have 3 different classes, 
#Warrior (Mid damage, Mid health), archer (High damage, low health), caster (Mid damage, low health, *Sorcs immune to magic*).


import random

class Hero:
    def __init__(self, player_name, level, max_health, player_class, strength, intelligence):
        self.name = player_name
        self.level = level
        self.type = player_class
        self.health = max_health
        self.max_health = max_health
        self.strength = level + 7 if player_class == 'Warrior' else 0
        self.intelligence = level * 4 if player_class == 'Sorcerer' else 0
        self.is_dead = False
    

#print who your hero is along with all of their stats
    def __repr__(self):
        return '*Narrarator* \n{name}: You are a level {level} {type} and currently have {health} out of {maxhealth} health. Your stats are: {strength} Strength, {intelligence} Intelligence.'.format(name = self.name, level = self.level, type = self.type, health = self.health, maxhealth = self.max_health, strength = self.strength, intelligence = self.intelligence)

      
    def attack_gnoll(self, gnoll):
        if self.type == 'Warrior':
          print('You deal {damage} damage to {type} Gnoll.'.format(damage = self.strength, type = gnoll))
          if gnoll == 'Mage':
            mage_gnoll.gnoll_health -= self.strength
            mage_gnoll.die(warrior)
          else:
            brawler_gnoll.gnoll_health -= self.strength
          if brawler_gnoll.gnoll_health <= 0:
            brawler_gnoll.die(warrior)         
        else:
          print('You deal {damage} damage to {type} Gnoll.'.format(damage = self.intelligence, type = gnoll))
          if gnoll == 'Mage':
            mage_gnoll.gnoll_health -= self.intelligence
          if mage_gnoll.gnoll_health <= 0:
            mage_gnoll.die(sorcerer)
          else:
            brawler_gnoll.gnoll_health -= self.intelligence
          if brawler_gnoll.gnoll_health <= 0:
            brawler_gnoll.die(sorcerer)
         

# If health reaches 0 or below 0, set dead, game over.        
    def game_over(self):
        self.is_dead = True
        print('You died.')
      
# If enemy gnoll health <= 0, self.level + 1, health == max_health.
    def level_up(self):
        self.level += 1
        self.health == self.max_health
        if self.type == 'Warrior':
          self.strength = self.level + 7
        else:
          self.intelligence = self.level * 4
        print('Level up! You are now level {level}. Strength {strength}, Intelligence {intelligence}.'.format(level = self.level, strength = self.strength, intelligence = self.intelligence))
        print('You do a twirly spin into a disco finger as power courses through you.')



# Describing Gnolls - There are 2 types of Gnolls, Brawler(Mid Damage, mid health), Mage(Mid damage, low health, sorc immune). They only attack and die. 
#the player will encounter 2 instances of gnolls. After defeating one, a printed message ('you venture forth... and see 'type' Gnoll. Attack!) The first enconter should be Mage. 
class Gnoll:
    def __init__(self, health, level, type):
        self.gnoll_health = health + level
        self.gnoll_type = type
        self.gnoll_damage = 2 if self.gnoll_type == 'Mage' else 4 
        self.is_alive = True
        self.level = level
  

#Announce the Gnoll encounter and type.
    def __repr__(self):
        return 'The Gnolls of the westback mountains are a fierce opponent for any adventurer. This one in particular is a level {level} {type} gnoll with {health} health.'.format(level = self.level, type = self.gnoll_type, health = self.gnoll_health)
        

# Check that gnoll is still alive. The higher the gnoll health i.e Brawler == 7, Mage == 5, the less damage they do. As long as the Gnoll is above 1 health, they will attack the player.  
    def attack_player(self, hero):
        if self.gnoll_health >= 1:
          if self.gnoll_type == 'Mage' and hero.type == 'Sorcerer':
            print("{player} is immune to enemy mage's attack!".format(player = hero.name))
        else:   
          print('{player} takes {damage} damage from {type} Gnoll'.format(player = hero.name, damage = self.gnoll_damage, type = self.gnoll_type))
        hero.health -= self.gnoll_damage
        if hero.health <= 0:
          hero.health = 0
          hero.game_over()
      
# If the gnoll is killed, health == 0, print('You have slaughtered your foe....')Player should self.level + 1, self.heal, and next encounter should begin.
    def die(self, hero):
        if self.gnoll_health <= 0:
          self.gnoll_health == 0
          self.is_alive == False
          print('Enemy {type} Gnoll defeated by {player}.'.format(type = self.gnoll_type, player = hero.name))
          hero.level_up()


brawler_gnoll = Gnoll(7, 1, 'Brawler') 
mage_gnoll = Gnoll(5, 1, 'Mage')

player_name = input('Welcome to the world of Nautz. Please type your character name and press enter. ')
while player_name == '':
  player_name = input('Please provide a valid name.')

player_class = input('Greetings ' + player_name + '. Please choose your character class, Warrior or Sorcerer. ')

if player_class != 'Warrior' and player_class != 'Sorcerer':
  player_class = input('Player class incorrect. Please try again.')
if player_class == 'Warrior':
  warrior = Hero(player_name, 1, 6, 'Warrior', 8, 0)
  print(warrior)
if player_class == 'Sorcerer':
  sorcerer = Hero(player_name, 1, 6, 'Sorcerer', 0, 4)
  print(sorcerer)
  
warrior = Hero(player_name, 1, 6, 'Warrior', 8, 0)
sorcerer = Hero(player_name, 1, 6, 'Sorcerer', 0, 4)
player = [warrior, sorcerer]
player[0] = warrior
player[1] = sorcerer


begin_game = input('Shall we begin your journey through Dark Gnoll? Yes or No? ')
if begin_game != 'Yes' and begin_game != 'No':
  begin_game = input('Please enter Yes or No. ')

if begin_game == 'No':
  begin_game = input('Please enter Yes when ready. ')

if begin_game == 'Yes':
  print('You begin your quest walking down a narrow cave. As you turn the corner you hear a stange sound. You then spot a dark mass out of the corner of your eye. ')


roll_for_skill1 = input('You cant quite make out what the creature is. Please "roll" 1d8 and press enter. ')

while roll_for_skill1 != 'roll':
  roll_for_skill1 = input('Please type roll to roll for skill. ')

if roll_for_skill1 == 'roll':
  roll_check = random.randint(1, 8)
  if roll_check >= 1:
    print('You rolled ' + str(roll_check) + '. Pass!')
    mage_gnoll = Gnoll(5, 1, 'Mage')
    print(mage_gnoll)

attack_or_die = input('As you stare at each other intensely from mere feet away, your body tenses with anticipation. Will this Gnoll allow you to pass or will it lunge? You begin to move, whether to attack or walk around it peacefully, you need to decide. Attack or Pass? ')
while attack_or_die != 'Attack' and attack_or_die != 'Pass':
  attack_or_die = input('Please choose to Attack or Pass. ')

if attack_or_die == 'Attack':
  if player_class == 'Warrior':
    warrior.attack_gnoll('Mage')
  else:
    sorcerer.attack_gnoll('Mage')
    print('The Gnoll reels in pain and lashes out with fireball!')
    mage_gnoll.attack_player(sorcerer)
    
if attack_or_die == 'Pass':
  if player_class == 'Sorcerer':
    print('The Mage Gnoll jumps at you as you try to pass it and grabs you by the throat and casts Burning Hands.')
    mage_gnoll.attack_player(sorcerer)
  if player_class == 'Warrior':  
    print('The Mage Gnoll jumps at you as you try to pass it and grabs you by the throat and casts Burning Hands. A searing pain hits you. The light begins to fade and you feel your life force slowly slip away...')
    mage_gnoll.attack_player(warrior)
    mage_gnoll.attack_player(warrior)
    mage_gnoll.attack_player(warrior)

if player_class == 'Sorcerer':    
  while mage_gnoll.gnoll_health >= 0:  
    sorcerer.attack_gnoll('Mage')