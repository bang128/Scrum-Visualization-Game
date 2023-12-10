# customer-project-porygon
## Final Project Report

### Project Title
- Scrum Simulator
### Team Members (specify the role and responsibility of each member)
- Chengwu (Jason) Duan (Product Owner)
- Denes A. Lopez (Scrum Master)
- Vincent Tran (Teammate)
- Bang Ngoc Pham (Teammate)
### Project Objectives
- Provide a game that educates the player on the scrum process by simulating the interactions and responsibility of each role.
### Project Design
- Team goals: 
   - 1. Satisfy user stories proposed by the customer initially
   - 2. Complete user stories made by ourselves by the end of each sprint in order to avoid leaving any of them in product backlog
- User stories completed. We completed 42 stories for 236 points
### Implementation Details
- Programming Languages Used
   - 1. Python3
- Libraries or Tools Used
   - 1. Pycharm
   - 2. Pygame
   - 3. CircleCI
- Challenges and Solutions
   - 1.
     - Challenge: Pygame does not allows two windows at the same time and also there is no tool to directly create popups.
     - Solution: We made a rectangle inside the current window as if the rectangle is a popup with a "Close" button to close that "popup".
   - 2.
     - Challenge: If we used real-world time in the game, the user may take days or weeks to complete it.
     - Solution: We created the game time thanks to clock.tick() function in Pygame, so 1 minute in the real world is approximately 1 day in the game
### Testing
- We used Unit Test with test cases described below and in-Built CircleCI Integration Checks
- Test Cases
   - 1. Menu Pane
     - Clicking the start button will take user to the game
     - Clicking the settings button will take user to the settings section
     - Clicking the tutorial button will take user to the tutorial section
   - 2. Unlock new teammates
     - “Lock” buttons for the teammates that are being locked
     - Each “Lock” button is clickable to show the player requirement to unlock that teammate
     - Decrease $20 if the player chooses to unlock one locked teammate
   - 3. The set of 3 statistic buttons in Game pane
     - Clicking on the “Resource” panel will display “Team Morale”, “Money”, and “Velocity” statistics for the player to see.
     - Clicking on “Score” panel will display the current completed stories and the players score.
     - Clicking on the “Day & Time” panel will display current sprint, current day, current time in the game
   - 4. Sound on/off toggles
     - Music and sound effects are separated into two buttons
     - Muting/unmuting the music will be consistent throughout the whole game
     - Muting/unmuting the sound effect will be consistent throughout the whole game
### Project Highlights (Retrospective)
- Parts of the actual software you are proud of
   - 1. Having classes for seperate panes
   - 2. Creation of popup class
- Things you guys did as a team that you think worked really well
   - 1. We met very frequently to solve issues together.
   - 2. We always completed proposed user stories by the end of each sprint as we had expected before that sprint.
- Troubles that you ended up solving or finding.
   - 1. We found the CircleCI caused failure when using Pygame
### Things To Be Improved (Also Retrospective)
- Parts of the software that you would improve. 
   - 1. We would improve on the updating of the resources like team morale, money, velocity, customer satisfaction.
   - 2. Connect all the numerical values where each one would affect eachother.
   - 3. Make actions have an affect when performed like hosting scrum meetings, assign tasks, etc.
   - 4. More in depth user interaction within the tutorial pane to help improve the users understanding of the game.
- Parts of your teamwork/process that you would improve on in the future.
   - 1. We could have more in person meetings to improve our team dynamics even more.
   - 2. Follow more of a daily workflow process in order to be more efficient.
   - 3. More consistent and active communication in our discord group.
### Lessons Learned
- Advice you have for future COMP 129 students. 
   - 1. Plan early and code consistently. 
   - 2. Meet often to clarify mutual understanding of the project design.
   - 3. Don't be afraid to ask for help.
   - 4. Have a great understanding of the customers idea for the project. This will help greatly for planning and execution.
   - 5. Identify teams strength and weaknesses.
