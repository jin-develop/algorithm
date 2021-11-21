function solution(dartResult) {
  let array = [];
  let j = 0;

  for (let i = 0; i < dartResult.length; i++) {
    if (-1 < parseInt(dartResult[i], 10) && parseInt(dartResult[i], 10) < 10) {
      array.push(j);
      if (dartResult[i] === '1') {
        if (dartResult[i + 1] === '0') {
          i = i + 1;
          j = 10;
          continue;
        }
      }
      j = +dartResult[i];
    }

    if (dartResult[i] === 'S') j = j ** 1;
    if (dartResult[i] === 'D') j = j ** 2;
    if (dartResult[i] === 'T') j = j ** 3;
    if (dartResult[i] === '*') {
      let poped = array.pop();
      array.push(poped * 2);
      j = j * 2;
    }
    if (dartResult[i] === '#') j = j * -1;
  }
  array.push(j);
  let sum = 0;
  for (let i = 0; i < array.length; i++) {
    sum += array[i];
  }
  return sum;
}
