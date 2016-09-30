Feature: Filter users by interest
  As a standard user
  I want to filter users by their listed interests
  So I can find users who have similar interests to my own

  Background: There are interests and users in the system
    Given there are a number of interests:
      | interest        |
      | Django          |
      | Testing         |
      | Public Speaking |
      | DevOps          |
      | PHP             |

    And there are many users, each with different interests:
      | name          | email       | interests               |
      | Billie Jean   | bj@test.com | Django, Testing         |
      | Rocky Raccoon | rc@test.com | Django, Public Speaking |
      | Major Tom     | mt@test.com | Testing, Devops         |
      | Bobbie McGee  | Bm@test.com | Public Speaking, DevOps |

  Scenario Outline: Filter users
    Given I am a logged un user
    When I filter the list of users by "<filter>"
    Then I see "<num>" users

    Examples:
      | filter          | num |
      | Django          | 2   |
      | Django, Testing | 3   |
      | PHP             | 0   |

