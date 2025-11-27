function test3(c) {
  return [1,2,3,4,5];
}

let c = [9, 9, 9];
c = test3(c);
console.log(c); // [1,2,3,4,5]


function userInfo(name, age, city) {
    return console.log(name, age, city)
}

userInfo('이름', 123, '천안')

n = 10
sum = 0
for(let i=1; i <= n; i++) {
    if(i % 2 == 0) {
        sum += i
    }
}
console.log(sum)

n = 5
for(let i = 0; i < n; i++) {
  const plus = '+'.repeat(n - 1 - i);
  const star = '*'.repeat(2 * i + 1);
  const dash = '-'.repeat(n - 1 - i);

  console.log(plus + star + dash);
}

arr=[]
for(let i=1; i < 7; i++) {
    for(let j=i; j <7; j++){
        arr.push([i][j])       
    }
}
console.log(arr.length)

function printNumber(n) {
  for (let i = 1; i <= n; i++) {
    process.stdout.write(i + " ");

    if (i % 3 === 0) {
      console.log();
    }
  }

  console.log();
}

printNumber(10);


const asdf = 20;
console.log(asdf)


let b = 20;


this


