function flat(arr) {
  const ar = [];

  for (let i = 0; i < arr.length; i++) {
    if (Array.isArray(arr[i])) {
      ar.push(...flat(arr[i]));
    } else {
      ar.push(arr[i]);
    }
  }

  return ar;
}

const f = flat([[1, [2, [3, 4]]]]);
console.log(f);
