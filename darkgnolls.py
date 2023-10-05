# Dark Gnolls - We have a "Hero" Class who can be 2 different classes, Warrior, Sorcerer, Rogue. 
#There are 2 basic stats, Strength, Int. Level ups happen every enemy killed and the player fully heals and stats should increase. 
#We have our main enemy "Gnolls" who have 3 different classes, 
#Warrior (Mid damage, Mid health), archer (High damage, low health), caster (Mid damage, low health, *Sorcs immune to magic*).
#for future iterations on this: Make attack roll rng for chance + damage.
print(""" 
      # # # # #     # # # # # #   # # # # #    #    #         # # # #    #       #      # # # #     #           #            # # # #    
      #        #    #         #   #        #   #   #         #           # #     #    #         #   #           #          #      
      #         #   #         #   #        #   #  #         #            #  #    #   #           #  #           #          #
      #         #   # # # # # #   # # # # #    # #          #            #   #   #   #           #  #           #           # # # # 
      #         #   #         #   #   #        # #          #    # # #   #    #  #   #           #  #           #                   # 
      #         #   #         #   #    #       #  #         #         #  #     # #    #         #   #           #                    # 
      #        #    #         #   #     #      #   #        #         #  #      ##     #       #    #           #                    #
      # # # # #     #         #   #      #     #    #        # # # # #   #       #      # # # #     # # # # #   # # # # #   # # # # #      
      """)

print("*Narrator* \nYou're finally awake. As you push yourself up off the cold and wet dirt you notice blood soaked into your clothes. You panic and begin checking yourself for injuries but your vision is pulled away to the body of a gnoll laying dead next to you, it's heart pierced by your dagger. Evidently you just managed to pull yourself out of the literal jaws of fate. You can't remember anything except that you know you need to travel to the city of Goteem. Why? You can't recall. Where is it? Who knows. But more importantly... who are you?...\n")
import random
import sys

class Hero:
    def __init__(self, player_name, level, health, max_health, player_class, strength, intelligence):
        self.name = player_name
        self.level = level
        self.type = player_class
        self.health = health
        self.max_health = max_health
        self.strength = level + 7 if player_class == 'Warrior' else 0
        self.intelligence = level * 4 if player_class == 'Sorcerer' else 0
        self.is_dead = False
      
    

#print who your hero is along with all of their stats
    def __repr__(self):
        return '\n*Narrarator* \n{name}: You are a level {level} {type} and currently have {health} out of {maxhealth} health. Your stats are: {strength} Strength, {intelligence} Intelligence.'.format(name = self.name, level = self.level, type = self.type, health = self.health, maxhealth = self.max_health, strength = self.strength, intelligence = self.intelligence)

      
    def attack_gnoll(self, gnoll):
        if self.type == 'Warrior':
          print('You deal {damage} damage to {type} Gnoll!'.format(damage = self.strength, type = gnoll))
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
        sys.exit()
      
# If enemy gnoll health <= 0, self.level + 1, health == max_health.
    def level_up(self):
        self.level += 1
        if self.type == 'Warrior':
          self.strength = self.level + 7
          self.max_health += 7
          self.health = self.max_health
        else:
          self.intelligence = self.level * 4
          self.max_health += 4
          self.health = self.max_health
        print('Level up! You are now level {level}. Strength {strength}, Intelligence {intelligence}, Health {health}/{maxhealth}.'.format(level = self.level, strength = self.strength, intelligence = self.intelligence, health = self.health, maxhealth = self.max_health))
        print('You do a twirly spin into a disco finger as power courses through you.')

#rest to heal damage
    def rest(self):
      self.health = self.max_health
      print('{player} awakens a short time later feeling refreshed. Current health is {health}/{maxhealth}.'.format(player = self.name, health = self.health, maxhealth = self.max_health))

# exhaustion damage
    def exhausted(self):
      self.health -= 1
      print('Your body fights you with every step but you push on. You suffer one damage: {health}/{maxhealth}.'.format(health=self.health, maxhealth=self.max_health))

# if loot lust goes wrong
    def trap_damage(self):
       damage = 2
       self.health -= damage
       print('You take {damage} damage from the trap. You now have {health} health.'.format(damage = damage, health = self.health))

    def ring_of_str(self):
      self.strength += 5
      print('Your total strength is now {strength}.'.format(strength = self.strength))
    
    def helm(self):
      self.intelligence += 4
      print('Your total intelligence is now {intelligence}.'.format(intelligence = self.intelligence))

# Describing Gnolls - There are 2 types of Gnolls, Brawler(Mid Damage, mid health), Mage(Mid damage, low health, sorc immune). They only attack and die. 
#the player will encounter 2 instances of gnolls. After defeating one, a printed message ('you venture forth... and see 'type' Gnoll. Attack!) The first enconter should be Mage. 
class Gnoll:
    def __init__(self, health, level, damage, type):
        self.gnoll_health = health + level
        self.gnoll_type = type
        self.gnoll_damage = damage 
        self.is_alive = True
        self.level = level
  

#Announce the Gnoll encounter and type.
    def __repr__(self):
        return '\nThe Gnolls of the westback mountains are a fierce opponent for any adventurer. This one in particular is a level {level} {type} gnoll with {health} health.'.format(level = self.level, type = self.gnoll_type, health = self.gnoll_health)
        

# Check that gnoll is still alive. The higher the gnoll health i.e Brawler == 7, Mage == 5, the less damage they do. As long as the Gnoll is above 1 health, they will attack the player.  
    def attack_player(self, hero):
        if self.gnoll_health >= 1:
          if (self.gnoll_type == 'Mage') and (hero.type == 'Sorcerer'):
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


brawler_gnoll = Gnoll(10, 1, 6, 'Brawler') 
mage_gnoll = Gnoll(5, 1, 2, 'Mage')

player_name = input('Welcome to the world of Nautz. Please type your character name and press enter. \n')
while player_name == '':
  player_name = input('Please provide a valid name.')

player_class = input('Greetings ' + player_name + '. Please choose your character class, Warrior or Sorcerer. \n')

if player_class != 'Warrior' and player_class != 'Sorcerer':
  player_class = input('Player class incorrect. Please try again.')
if player_class == 'Warrior':
  warrior = Hero(player_name, 1, 6, 6, 'Warrior', 8, 0)
  print(warrior)
if player_class == 'Sorcerer':
  sorcerer = Hero(player_name, 1, 6, 6, 'Sorcerer', 0, 4)
  print(sorcerer)
  
warrior = Hero(player_name, 1, 6, 6, 'Warrior', 8, 0)
sorcerer = Hero(player_name, 1, 6, 6, 'Sorcerer', 0, 4)
player = [warrior, sorcerer]
player[0] = warrior
player[1] = sorcerer


begin_game = input('Shall we begin your journey through Dark Gnoll? Yes or No? \n')
if begin_game != 'Yes' and begin_game != 'No':
  begin_game = input('Please enter Yes or No. ')

if begin_game == 'No':
  begin_game = input('Please enter Yes when ready. ')

if begin_game == 'Yes':
  print('\nYou begin your quest walking down a narrow cave. As you turn the corner you hear a stange sound. You then spot a dark mass out of the corner of your eye. ')


roll_for_skill1 = input('You cant quite make out what the creature is. Please "Roll" 1d8 (+ int bonus) and press enter. \n')
while roll_for_skill1 != 'Roll':
  roll_for_skill1 = input('Please type Roll to roll for skill. ')
if roll_for_skill1 == 'Roll':
  if player_class == 'Warrior':
    war_roll_check = random.randint(1, 8)
    if war_roll_check >= 4:
        print('You rolled ' + str(war_roll_check) + '. Pass!')
        mage_gnoll = Gnoll(5, 1, 2, 'Mage')
        print(mage_gnoll)
    else:
        print('\nShame, you rolled ' + str(war_roll_check) + '. You notice nothing out of the ordinary.')  
  else:  
    sorc_roll_check = random.randint(1, 8) + sorcerer.intelligence
    if sorc_roll_check >= 4:
        print('You rolled ' + str(sorc_roll_check) + '. Pass!')
        mage_gnoll = Gnoll(5, 1, 2, 'Mage')
        print(mage_gnoll)  
    else:
        print('\nShame, you rolled ' + str(sorc_roll_check) + '. You notice nothing out of the ordinary.')  

attack_or_die = input('As you stare at each other intensely from mere feet away, your body tenses with anticipation. Will it allow you to pass or will it lunge? You begin to move, whether to attack or walk around it peacefully, you need to decide. Attack or Pass? \n')
while attack_or_die != 'Attack' and attack_or_die != 'Pass':
  attack_or_die = input('Please choose to Attack or Pass. ')
if attack_or_die == 'Attack':
  if player_class == 'Warrior':
    print('\n')
    warrior.attack_gnoll('Mage')
  else:
    print('\n')
    sorcerer.attack_gnoll('Mage')
    print('The Gnoll reels in pain and lashes out with fireball!')
    mage_gnoll.attack_player(sorcerer)
    sorcerer.attack_gnoll('Mage')
if attack_or_die == 'Pass':
  if player_class == 'Sorcerer':
    print('\n')
    print('The Mage Gnoll jumps at you as you try to pass it and grabs you by the throat and casts Burning Hands.')
    mage_gnoll.attack_player(sorcerer)
    sorcerer.attack_gnoll('Mage')
    if mage_gnoll.gnoll_health >= 0:
        print('Enemy Mage Gnoll is dazed!')
        sorcerer.attack_gnoll('Mage')
  if player_class == 'Warrior':
    print('\n')  
    print('The Mage Gnoll jumps at you as you try to pass it and grabs you by the throat and casts Burning Hands. A searing pain hits you. The light begins to fade and you feel your life force slowly slip away...')
    warrior.game_over()     
    

cont_journey = input('Continue your journey? Yes or No? \n')
while cont_journey != 'Yes' and cont_journey != 'No':
   cont_journey = input('Please type Yes or No. ')
if cont_journey == 'No':
  cont_journey = input('Please type Yes when ready otherwise type exit() to exit the game. \n')
if cont_journey == 'Yes':
  print('\nIts a long journey to the other end of the cave. Your boots are soaked and worn and your body exhausted. After what feels like days of crouching through the narrow system you spot a glimmer of light in front of you and smell fresh air. You draw closer to the cave exit when all of a sudden you kick something hard at your feet. A chest, probably belonging to the Gnoll you just threw down. You go to reach for it but stop short. Could it be a trap?')
  chest1 = input('Do you "Reach" to open the chest or "Check" its surroundings first? \n')

while (chest1 != 'Reach') and (chest1 != 'Check'):
   chest1 = input('Please type Reach or Check. \n')
if chest1 == 'Reach':
  chest_reach_war = input('\nYou reach out in blind lust to open the chest and feel a wire cross the back of your hand as the lid swings open. Suddenly a loud whip-like sound cracks the air. "Roll" 1d20 (+ str bonus) to dodge. \n')
  while chest_reach_war != 'Roll':
    chest_reach_war = input('Please type Roll to roll. ')
  if chest_reach_war == 'Roll':
    if player_class == 'Warrior':
      dodge_roll = random.randint(1, 20) + warrior.strength
      if dodge_roll <= 14:
        print('\n')
        print('You rolled ' + str(dodge_roll) + ', Fail! Your right shoulder erupts in pain as you fall to the floor. In your lust for loot you missed the obvious wire trap connected to a series of throw darts behind you.')
        warrior.trap_damage()
        print('You slowly regain your composure and pick yourself up.')
      else:
        print('\n')
        print('You rolled ' + str(dodge_roll) + ', Pass! You narrowly step out of the way as 3 throwing darts inch past your right shoulder and embed themselevs into the wall.')
      print('\nYou peer into the contents of the chest and pick out something shiny - a "Ring of Precise Attack!" (+4 to strength). You put it on and immediately feel stonger.')
      warrior.ring_of_str()
      
    else:
      dodge_roll = random.randint(1, 20)
      if dodge_roll <= 14:
        print('\n')
        print('You rolled ' + str(dodge_roll) + ', Fail! Your right shoulder erupts in pain as you fall to the floor. In your lust for loot you missed the obvious wire trap connected to a series of throw darts behind you.')
        sorcerer.trap_damage()
        print('You slowly regain your composure and pick yourself up.')
      else:
        print('\n')
        print('You rolled ' + str(dodge_roll) + ', Pass! You narrowly step out of the way as 3 throwing darts inch past your right shoulder and embed themselevs into the wall.')
      print('\nYou peer into the contents of the chest and pick out something shiny - a "Helm of Intelligence" (+4 to intelligence). You put it on and immediately feel wiser.')
      sorcerer.helm()

if chest1 == 'Check':
  chest_check_war = input('Your eyes scan the area for signs of ill intent. Roll 1d20 (+ intelligence bonus). \n')
  while chest_check_war != 'Roll':
    chest_check_war = input('Please type Roll to roll. \n')
  if chest_check_war == 'Roll':
    if player_class == 'Warrior':
      check_roll = random.randint(1, 20)
      if check_roll <= 14:
        print('\n')
        print('You rolled ' + str(check_roll) + ', Fail! Your gaze gets stuck on a grouping of unremarkable rocks. Assuming you are clear, you reach for the top of the chest. A loud *crack* breaks the silent air. Your right shoulder erupts in pain as you fall to the floor with three darts embedded in your back.')
        warrior.trap_damage()
        print('You slowly regain your composure and pick yourself up.')
      else:
        print('\n')
        print('You rolled ' + str(check_roll) + ', Pass! You notice a thin wire wrapped between the handle of the chest, laying just taught enough across the ground. It connects to a series of holes in the wall behind you. You step away and surgically cut the wire from a distance as 3 darts explode out of the holes and embed themselves in the far wall.')
      print('\nAs you peer into the contents of the chest you pick out something shiny - a "Ring of Precise Attack!" (+5 to strength). You put it on and immediately feel stonger.')
      warrior.ring_of_str()  
    else:
      check_roll = random.randint(1, 20) + sorcerer.intelligence
      if check_roll <= 14:
        print('\n')
        print('You rolled ' + str(check_roll) + ', Fail! Your gaze gets stuck on a grouping of unremarkable rocks. Assuming you are clear, you reach for the top of the chest. A loud *crack* breaks the silent air. Your right shoulder erupts in pain as you fall to the floor with three darts embedded in your back.')
        sorcerer.trap_damage()
        print('You slowly regain your composure and pick yourself up.')
      else:
        print('\n')
        print('You rolled ' + str(check_roll) + ', Pass! You notice a thin wire wrapped between the handle of the chest, laying just taught enough across the ground. It connects to a series of holes in the wall behind you. You step away and surgically cut the wire from a distance as 3 darts explode out of the holes and embed themselves in the far wall.')
      print('\nAs you peer into the contents of the chest you pick out something shiny - a "Helm of Intelligence" (+4 to intelligence). You put it on and immediately feel wiser.')
      sorcerer.helm()

venture_forth = input('\nWith your powers strengthened, you exit the cave and inhale a deep breath of fresh air. All of a sudden you feel the weight of your pack and the cold in your bones. Exhaustion grips you. On a hill nearby you spot a perfect place to setup camp. You may "Rest" or "Continue" on. \n')
while (venture_forth != 'Rest') and (venture_forth != 'Continue'):
  venture_forth = input('Please type Rest or Continue. ')
if venture_forth == 'Rest':
  if player_class == 'Warrior':
    warrior.rest()
  else:
    sorcerer.rest()
if venture_forth == 'Continue':
  if player_class == 'Warrior':
    warrior.exhausted()
  else:
    sorcerer.exhausted()

dodge_gnoll = input('\nYou make your way down the hillside north and spot the towers of Goteem city! As you pick up your pace the sound of your pack blocks out the sounds of the mountainside. "Roll" 1d20 (+ strength bonus). \n')
while dodge_gnoll != 'Roll':
  dodge_gnoll = input('Please type Roll. ')
if dodge_gnoll == 'Roll':
  if player_class == 'Warrior':
    dodge_gnoll2 = random.randint(1, 20) + warrior.strength
    if dodge_gnoll2 <= 10:
      print('\n')
      print('You rolled ' + str(dodge_gnoll2) + ', Fail! The noise of your pack covers the sound of a large Brawler Gnoll charging at you down the mountain. With one sweep of its arms it sends you careening 50 feet down the hill.')
      brawler_gnoll.attack_player(warrior)
      print('Fortunately you landed face first in the snow. You manage to get yourself up in time to see the beast coming for you a second time.You draw your weapon.')
    else:
      print('\n')
      print('You rolled ' + str(dodge_gnoll2) + ', Pass! You feel a shaking of the ground below you. Your quick reflexes allow you to jump out of the way as a massive Brawler Gnoll throws its entire body weight into where you were just standing. As it turns around, you take in the true size of the beast and steel yourself for battle.')
  if player_class == 'Sorcerer':
    dodge_gnoll2 = random.randint(1, 20)
    if dodge_gnoll2 <= 10:
      print('\n')
      print('You rolled ' + str(dodge_gnoll2) + ', Fail! The noise of your pack covers the sound of a large Brawler Gnoll charging at you down the mountain. With one sweep of its arms it sends you careening 50 feet down the hill.')
      brawler_gnoll.attack_player(sorcerer)
      print('Fortunately you landed face first in the snow. You manage to get yourself up in time to see the beast coming for you a second time.You draw your weapon.')
    else:
      print('\n')
      print('You rolled ' + str(dodge_gnoll2) + ', Pass! You feel a shaking of the ground below you. Your quick reflexes allow you to jump out of the way as a massive Brawler Gnoll throws its entire body weight into where you were just standing. As it turns around, you take in the true size of the beast and steel yourself for battle.')

attack_gnoll = input('As you meet the beasts eyes you see that you have only one chance to smite him or he will tear into your body with both fangs and claws. You prepare to deal one swift and deadly blow. "Roll" to attack (+ intelligence, + strength). \n')
while attack_gnoll != 'Roll':
  attack_gnoll = input('Please type Roll. ')
if attack_gnoll == 'Roll':
  if player_class == 'Warrior':
    attack_gnoll = random.randint(1, 20) + warrior.strength
    if attack_gnoll <= 14:
      print('\n')
      print('You rolled ' + str(attack_gnoll) + ', Fail! You swing at the beast with all your might but its too quick. It leaps back before swiping a large, clawed hand at your body.')
      brawler_gnoll.attack_player(warrior)
        
      attack_gnoll_again = input('You take a gasp of air and clutch your bloodied torso. The beast is in range. Its now or never. Roll to attack. \n')
      while attack_gnoll_again != 'Roll':
        attack_gnoll_again = input('Please type Roll. ')
      if attack_gnoll_again == 'Roll':
        final_roll = random.randint(1, 20) + warrior.strength
        if final_roll <= 10:
          print('\n')
          print('You rolled ' + str(final_roll) + ', Fail! You flail your weapon in desperation but the Brawler Gnoll catches it mid swing. He stares at you as you are held frozen by him. Is that a smile you see?')
          brawler_gnoll.attack_player(warrior)
        else:
          print('\n')
          print('You rolled ' + str(final_roll) + ', Pass! With one final desperate swing of your weapon, you thrust into the side of the gnolls neck.')
          warrior.attack_gnoll('Brawler')
          print('You watch as the gnoll falls lifelss to the ground and slowly slides down the moutainside.')
    else:
      print('\n')
      print('You rolled ' + str(attack_gnoll) + ', Pass! You muster up every bit of strength in your body and swing your weapon as hard as you can. You feel it connect with the gnolls neck and pass through it cleanly and thoroughly.')
      warrior.attack_gnoll('Brawler')
      print('You watch as the gnoll falls lifelss to the ground and slowly slides down the moutainside.')

  if player_class == 'Sorcerer':
    attack_gnoll2 = random.randint(1, 20) + sorcerer.intelligence
    if attack_gnoll2 <= 14:
      print('\n')
      print('You rolled ' + str(attack_gnoll2) + ', Fail! You swing at the beast with all your might but its too quick. It leaps back before swiping a large, clawed hand at your body.')
      brawler_gnoll.attack_player(sorcerer)
      
    
      attack_gnoll_again1 = input('You take a gasp of air and clutch your bloodied torso. The beast is in range. Its now or never. Roll to attack. ')
      while attack_gnoll_again1 != 'Roll':
        attack_gnoll_again1 = input('Please type Roll. ')
      if attack_gnoll_again1 == 'Roll':
        final_roll1 = random.randint(1, 20) + warrior.strength
        if final_roll1 <= 10:
          print('\n')
          print('You rolled ' + str(final_roll1) + ', Fail! You flail your weapon in desperation but the Brawler Gnoll catches it mid swing. He stares at you as you are held frozen by him. Is that a smile you see?')
          brawler_gnoll.attack_player(sorcerer)
        else:
          print('\n')
          print('You rolled ' + str(final_roll1) + ', Pass! With one final desperate swing of your weapon, you thrust into the side of the gnolls neck.')
          sorcerer.attack_gnoll('Brawler')
          print('You watch as the gnoll falls lifelss to the ground and slowly slides down the moutainside.')
    else:
      print('\n')
      print('You rolled ' + str(attack_gnoll2) + ', Pass! You muster up every bit of strength in your body and swing your weapon as hard as you can. You feel it connect with the gnolls neck and pass through it cleanly and thoroughly.')
      sorcerer.attack_gnoll('Brawler')
      print('You watch as the gnoll falls lifelss to the ground and slowly slides down the moutainside.')
