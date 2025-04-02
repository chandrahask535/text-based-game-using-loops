Text-based Adventure Game Development

# README: "Text-based Adventure Game"(TASK 2)

## Author: CHANDRAHAS K

## Batch:(5th NOVEMBER- 5th DECEMBER)

## Domain: PYTHON Programming

## Aim

 To design and develop a text-based adventure game in Python. This project offers a fantastic opportunity to hone your programming skills, particularly in game development and user interaction.


## Description

Text-based Adventure Game in Python: Embark on an interactive journey with a captivating storyline, immersive user choices, and multiple endings.

## Libraries Used

The following important libraries were used for this project:
-random

  ## Working of the Code:

1. **Introduction and Starting Point:**
   - The game begins with an introduction in the `introduction` function.
   - The player is a wildlife police officer tasked with rescuing a lost child.

2. **Choosing a Path:**
   - The `choose_path` function presents the player with a choice: to go 'forward' into a dense forest or 'downward' through a secret tunnel.

3. **Dense Forest Scenario:**
   - If the player chooses the dense forest, they enter the `dense_forest` function.
   - Encounter a grizzly bear and make choices that can lead to finding the lost child or facing challenges like bats and landslides.

4. **Bats Encounter:**
   - After navigating the dense forest, the player may encounter bats in the `dense_forest_bats` function.
   - Choices include 'stay_calm' or 'use_flashlight' to proceed.

5. **Landslide Challenge:**
   - After the bat encounter, the player faces a potential landslide in the `dense_forest_landslide` function.
   - Choices include 'climb_up' or 'slide_down,' each leading to different consequences.

6. **Continuation in the Dense Forest:**
   - Depending on choices made, the player reaches the `dense_forest_continued` function, where they eventually find the lost child.

7. **Secret Tunnel Scenario:**
   - If the player chooses the secret tunnel at the beginning, they enter the `secret_tunnel` function.
   - Similar to the dense forest, the player faces choices involving bats and a potential landslide.

8. **Continuation in the Secret Tunnel:**
   - After navigating the secret tunnel, there's a chance of finding the lost child in the `secret_tunnel_continued` function.

9. **Alternative Ending:**
   - If the player doesn't find the child, they reach the `alternative_ending` function, resulting in an unsuccessful mission.

10. **Rescue and Mission Completion:**
   - If the player finds the child, they enter the `lost_child_location` function, where they must choose to 'call_for_help' or 'rescue_alone.'
   - The mission can be successfully completed in the `mission_complete` function.

The `main` function orchestrates the flow of the game, continuously updating the player's location based on their choices until the game concludes. The code provides an interactive and dynamic text-based adventure with multiple possible outcomes.
