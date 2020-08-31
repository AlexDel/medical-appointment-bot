## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- heu

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- buy

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?
- who are you?

## intent:thanks
- thank you
- thanks
- oh good, thanks
- thanks you

## intent:complain
- my [leg](part_of_body) hurts
- I sprain my [ankle]{"entity": "part_of_body", "value": "leg"}
- My [foot]{"entity": "part_of_body", "value": "leg"} hurts
- I think I pulled my [leg](part_of_body)
- my [ankle]{"entity": "part_of_body", "value": "leg"} hurts
- I felt a twinge in my [heart](part_of_body)
- i have [chest]{"entity": "part_of_body", "value": "heart"} Discomfort
- i feel [heartburn]{"entity": "part_of_body", "value": "heart"}
- i feel that my [heart](part_of_body) beats irregulary
- my [heart](part_of_body) hurts
- also i feel [chest]{"entity": "part_of_body", "value": "heart"} burn
- my [ankle]{"entity": "part_of_body", "value": "leg"} herts
- my [heart](part_of_body) burns
- mu [ankle](part_of_body)[ankle]{"entity": "part_of_body", "value": "leg"} hurts
- my [ankles](part_of_body) hurts
- my [leg](part_of_body) gurts

## intent:telling_address
- 489 w. Wall Street NewYork

## intent:show_avaliabe_dates
- /show_avaliabe_dates

## intent:store_time
- /store_time{"time":"09:30:00"}

## synonym:heart
- chest
- heartburn

## synonym:leg
- ankle
- foot
