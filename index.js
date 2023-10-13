// TASK 1

// function pow (x, n) {
//     return (n == 1) ? x : (x * pow(x, n - 1));
// }
// alert (pow(2,2))

// TASK 2

// function max_div(a, b)
// { a > b || ([a, b] = [b, a]);
//   let length = b/2, k = 1;
//   for (var i = 2; i <= length; ) {
//       if(!(b % i) && !(a % i) ) {
//       b /= i;
//       a /= i;
//       k *= i;
//       }
//       else i++
//   }
//   return k
// }
// alert(max_div(60, 30));

// TASK 3

// function findMax(number) {
//     if (number < 10) return number;
//     return Math.max(number % 10, findMax(parseInt(number / 10)));
//   }

// alert(findMax(123846035));

// TASK 4

// function isPrime(num) {
//     for (let i = 2; i < num; i++) {
//       if (num % i == 0) return false;
//     }
//     return num != 1;
//   }

// alert(isPrime(5))

// TASK 5

// function factor(n){
//     ans = []
//     d = 2
//     while (d * d <= n){
//         if (n % d == 0){
//             ans.push(d)
//             n/=d }
//         else{
//             d += 1}
//     }
//     if (n > 1){
//         ans.push(n)
//     }
//     return ans
// }
// alert(factor(18))

// TASK 6

function fib (n) {
    return n <= 1 ? n : fib(n - 1) + fib(n - 2);
  }
  
  alert(fib(6));