function solution(participant, completion) {
  // var answer = '';
  // for(let x of participant) {
  //     if(completion.indexOf(x) === -1) {
  //        answer = x
  //         return answer;
  //     } else {
  //         completion.splice(completion.indexOf(x), 1)
  //     }
  // }
  participant.sort()
  completion.sort()
  for(let i=0; i<completion.length; i++){
      if(participant[i] !== completion[i]) return answer=participant[i]
  }
  return participant[participant.length-1]
}