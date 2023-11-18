import random

def introduction():
    print("Welcome to the Wildlife Police Adventure!")
    print("You are a dedicated wildlife police officer, and today, you face a critical mission.")
    print("A child is lost in the vast wilderness, and it's your duty to find and rescue them.")

def choose_path():
    print("\nYou find a mysterious lever in front of a mountain. The lever is attached to a lift.")
    print("Do you want to push the lever 'forward' into the dense forest or 'downward' through a secret tunnel?")
    choice = input("Enter 'forward' or 'downward': ")
    if choice == "forward":
        return "dense_forest"
    elif choice == "downward":
        return "secret_tunnel"
    else:
        print("Invalid choice. Please enter 'forward' or 'downward'.")
        return choose_path()

def dense_forest():
    print("\nThe lift moves upward, taking you into the dense forest.")

    print("While exploring the forest, you hear mysterious sounds and notice shadows moving around you.")
    print("Suddenly, the forest becomes eerily silent.")

    print("As you investigate, you come face to face with a majestic, yet imposing, grizzly bear.")
    print("The bear stares at you but doesn't attack. It seems to be guarding something.")

    # Introduce a random chance of finding the child
    if random.choice([True, False]):
        print("\nYou notice the lost child behind a tree, unharmed but scared.")
        print("Options: 'calm_bear' or 'rescue_child'")
        choice = input("Enter 'calm_bear' or 'rescue_child': ")
        if choice == "calm_bear":
            print("\nWith a calm demeanor, you manage to communicate with the bear.")
            print("The bear allows you to leave the forest safely with the child.")
            return "lost_child_location"
        elif choice == "rescue_child":
            print("\nDespite the bear's imposing presence, you courageously rescue the child.")
            return "lost_child_location"
        else:
            print("Invalid choice. Please enter 'calm_bear' or 'rescue_child'.")
            return dense_forest()
    else:
        print("The bear roams off into the forest, allowing you to continue your journey.")
        return "dense_forest_bats"

def dense_forest_bats():
    print("\nWhile continuing your journey through the dense forest, you encounter a colony of bats.")

    print("Options: 'stay_calm' or 'use_flashlight'")
    choice = input("Enter 'stay_calm' or 'use_flashlight': ")
    if choice == "stay_calm":
        print("\nYour calm demeanor prevents the bats from attacking. You continue deeper into the forest.")
        return "dense_forest_landslide"
    elif choice == "use_flashlight":
        print("\nThe bats are scared away by the flashlight. You continue deeper into the forest.")
        return "dense_forest_landslide"
    else:
        print("Invalid choice. Please enter 'stay_calm' or 'use_flashlight'.")
        return dense_forest_bats()

def dense_forest_landslide():
    print("\nAs you venture further, you encounter a steep slope prone to landslides.")

    print("Options: 'climb_up' or 'slide_down'")
    choice = input("Enter 'climb_up' or 'slide_down': ")
    if choice == "climb_up":
        print("\nCautiously, you climb up the slope and avoid the potential landslide.")
        return "dense_forest_continued"
    elif choice == "slide_down":
        print("\nYou decide to slide down the slope, and suddenly, a landslide begins!")
        print("Options: 'brace_for_impact' or 'try_to_avoid'")
        choice = input("Enter 'brace_for_impact' or 'try_to_avoid': ")
        if choice == "brace_for_impact":
            print("\nYou brace for impact and manage to survive the landslide.")
            return "dense_forest_continued"
        elif choice == "try_to_avoid":
            print("\nYou try to avoid the falling debris, but unfortunately, you get injured.")
            print("Despite the setback, you continue your journey.")
            return "dense_forest_continued"
        else:
            print("Invalid choice. Please enter 'brace_for_impact' or 'try_to_avoid'.")
            return dense_forest_landslide()
    else:
        print("Invalid choice. Please enter 'climb_up' or 'slide_down'.")
        return dense_forest_landslide()

def dense_forest_continued():
    print("\nYou continue your journey, the atmosphere tense, and eventually, you find the lost child.")
    return "lost_child_location"

def secret_tunnel():
    print("\nThe lift moves downward, revealing a hidden tunnel.")

    print("As you traverse the tunnel, you encounter a colony of bats.")

    print("Options: 'stay_calm' or 'use_flashlight'")
    choice = input("Enter 'stay_calm' or 'use_flashlight': ")
    if choice == "stay_calm":
        print("\nYour calm demeanor prevents the bats from attacking. You continue deeper into the tunnel.")
        return "secret_tunnel_landslide"
    elif choice == "use_flashlight":
        print("\nThe bats are scared away by the flashlight. You continue deeper into the tunnel.")
        return "secret_tunnel_landslide"
    else:
        print("Invalid choice. Please enter 'stay_calm' or 'use_flashlight'.")
        return secret_tunnel()

def secret_tunnel_landslide():
    print("\nAs you progress through the tunnel, you encounter a section prone to landslides.")

    print("Options: 'brace_for_impact' or 'find_alternative_route'")
    choice = input("Enter 'brace_for_impact' or 'find_alternative_route': ")
    if choice == "brace_for_impact":
        print("\nYou brace for impact and successfully navigate through the landslide.")
        return "secret_tunnel_continued"
    elif choice == "find_alternative_route":
        print("\nYou decide to find an alternative route, avoiding the potential landslide.")
        return "secret_tunnel_continued"
    else:
        print("Invalid choice. Please enter 'brace_for_impact' or 'find_alternative_route'.")
        return secret_tunnel_landslide()

def secret_tunnel_continued():
    print("\nYou continue your journey through the secret tunnel.")

    # Introduce a random chance of finding the child
    if random.choice([True, False]):
        print("\nWhile exploring the tunnel, you discover the lost child!")
        return "lost_child_location"
    else:
        print("\nYou explore the tunnel but find no sign of the lost child.")
        return "alternative_ending"

def alternative_ending():
    print("\nUnfortunately, your search ends in vain, and you're unable to locate the lost child.")
    print("Thanks for playing the Wildlife Police Adventure!")
    exit()

def lost_child_location():
    print("\nYou locate the lost child in a precarious situation!")

    print("Options: 'call_for_help' or 'rescue_alone'")
    choice = input("Enter 'call_for_help' or 'rescue_alone': ")
    if choice == "call_for_help":
        print("\nYou call for backup, and together, you successfully rescue the lost child.")
        return "mission_complete"
    elif choice == "rescue_alone":
        print("\nDespite the challenges, you manage to rescue the child on your own. Well done!")
        return "mission_complete"
    else:
        print("Invalid choice. Please enter 'call_for_help' or 'rescue_alone'.")
        return lost_child_location()

def continue_mission():
    print("\nYou continue your mission through the secret tunnel.")

    print("Options: 'rescue_child' or 'explore_deeper'")
    choice = input("Enter 'rescue_child' or 'explore_deeper': ")
    if choice == "rescue_child":
        print("\nYou reach the end of the tunnel and successfully rescue the lost child.")
        return "mission_complete"
    elif choice == "explore_deeper":
        print("\nYou decide to explore deeper into the tunnel, uncovering more secrets.")
        return "treasure_chamber"
    else:
        print("Invalid choice. Please enter 'rescue_child' or 'explore_deeper'.")
        return continue_mission()

def mission_complete():
    print("\nCongratulations! You've successfully rescued the lost child and navigated the mysterious tunnel.")
    print("Your dedication as a wildlife police officer has made a positive impact!")

def game_over():
    print("\nThanks for playing the Wildlife Police Adventure!")
    exit()

def main():
    introduction()
    current_location = choose_path()

    while True:
        if current_location == "dense_forest":
            current_location = dense_forest()
        elif current_location == "dense_forest_bats":
            current_location = dense_forest_bats()
        elif current_location == "dense_forest_landslide":
            current_location = dense_forest_landslide()
        elif current_location == "dense_forest_continued":
            current_location = dense_forest_continued()
        elif current_location == "secret_tunnel":
            current_location = secret_tunnel()
        elif current_location == "secret_tunnel_landslide":
            current_location = secret_tunnel_landslide()
        elif current_location == "secret_tunnel_continued":
            current_location = secret_tunnel_continued()
        elif current_location == "alternative_ending":
            alternative_ending()
        elif current_location == "lost_child_location":
            current_location = lost_child_location()
        elif current_location == "continue_mission":
            current_location = continue_mission()
        elif current_location == "mission_complete":
            mission_complete()
            game_over()

if __name__ == "__main__":
    main()

