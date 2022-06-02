// With recursion
function condenseArr(arr) {
  if (arr.length === 1) {
    console.log(`${arr[0]}`);
    return;
  }

  let out = [];
  let sum = 0;

  for (let i = 0; i < arr.length; i++) {
    if (i === arr.length - 1) {
      break;
    } else {
      let sum = arr[i] + arr[i + 1];
      out.push(sum);
    }
  }

  if (out.length > 2) {
    condenseArr(out);
  } else {
    sum += out.reduce((acc, cur) => acc + cur, 0);
    console.log(sum);
  }
}

// With while loop

function condenseArr(arr) {
  if (arr.length === 1) {
    console.log(`${arr[0]}`);
    return;
  }

  let out = [];

  for (let i = 0; i < arr.length - 1; i++) {
    let cur = arr[i] + arr[i + 1];
    out.push(cur);
  }

  while (out.length > 1) {
    // You can create here a temporary array and at the end of the loop (in this loop you are filling the temporary array until the last element of the out array)
    //  reassing the out array with temporal one!
    // out = temp[]
    for (let k = 0; k < out.length - 1; k++) {
      let cur = out[k] + out[k + 1];
      out[k] = cur;
    }

    out.pop();
  }

  console.log(out.join(" "));
}
