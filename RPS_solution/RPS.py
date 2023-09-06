# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


play_order = {}

def compute(i, ar=['R', 'P', 'S'], tmp = []):
  if i == 4:
    play_order[''.join(tmp)] = 0 
  else:
    for x in ar:
      tmp.append(x)
      compute(i+1, ar, tmp)
      tmp.pop()

compute(0)
def player(prev_opponent_play,
          opponent_history=[]
         ):

    if not prev_opponent_play:
        prev_opponent_play = 'R'
        opponent_history.append(prev_opponent_play)  
        opponent_history.append(prev_opponent_play)  
    opponent_history.append(prev_opponent_play)

    last_two = "".join(opponent_history[-4:])
    if len(last_two) == 4:
        play_order[last_two] += 1
      
    
    potential_plays = [
        "".join(opponent_history[-3:]) + "R",
        "".join(opponent_history[-3:]) + "P",
        "".join(opponent_history[-3:]) + "S",
    ]
  
    
    sub_order = {
        k: play_order[k]
        for k in potential_plays if k in play_order
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]
