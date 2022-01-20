// cse220c_week_02_prove.cpp - Sample Solution
//

#include <algorithm>  // std::transform, std::remove_if, std::for_each
#include <iostream>   // std::cout, std::cin
#include <memory>     // std::unique_ptr
#include <numeric>    // std::accumulate

using namespace std; // avoids the need to use std:: in front of cin, cout, etc

// Function prototypes. Required if the function definitions come after main.
int calc_sum(int count, const unique_ptr<int[]>& numbers);
int find_min(int count, const unique_ptr<int[]>& numbers);
int find_max(int count, const unique_ptr<int[]>& numbers);

int main()
{
   int count = 0;

   cout << "How many numbers? ";
   cin >> count;

   // Set up an array to store the numbers. Notice the "new" keyword. This
   // allows us to allocate the appropriate amount of space at run time. In
   // this case, we are reserving memory for an array that can store
   // "count" number of integers and we will refer to that array using
   // a smart pointer called "numbers"
   unique_ptr<int[]> numbers(new int[count]);

   // Get numbers from console using a counting loop
   for (int i = 0; i < count; i++) {
      cout << "Number " << i + 1 << ": ";
      cin >> numbers[i];
   }

   // Calculate the sum, min, and max using reduce functionality by using the
   // accumulate function.

   auto numbers_end = numbers.get() + count;

   // Note the default behavior of accumulate is to add each element. So
   // we can find the sum of the numbers in the array like this:
   auto sum = accumulate(numbers.get(), numbers_end, 0);

   // Alternatively, we could use a lambda function to find the sum
   auto alternative_sum = accumulate(numbers.get(), numbers_end, 0,
      [](auto sum, auto number) { return sum + number; });


   // Calculate the average using the sum. Note we need to explicitly
   // cast one of the variables in the calculation to a floating point number
   // or we will end up doing integer division instead of floating point
   // division
   auto average = sum / (float)count;

   // Calculate the min using accumulate with a lambda function
   auto min = accumulate(numbers.get(), numbers_end, numbers[0],
      [](auto min, auto number) {
      return (number < min) ? number : min;
      });

   // Calculate the max using accumulate with a lambda function
   auto max = accumulate(numbers.get(), numbers_end, numbers[0],
      [](auto max, auto number) {
      return (number > max) ? number : max;
      });

   cout << endl;
   cout << "Sum: " << sum << endl;
   cout << "Average: " << average << endl;
   cout << "Minimum: " << min << endl;
   cout << "Maximum: " << max << endl;


   // Square all numbers in the list using map (transform)
   numbers_end = numbers.get() + count;
   numbers_end = transform(numbers.get(), numbers_end, numbers.get(),
      [](auto x) { return x * x; });
   cout << "Square of each number:";
   for_each(numbers.get(), numbers_end, [](auto x) { cout << " " << x; });
   cout << endl;

   // Find all numbers less than 1000 using filter (remove_if)
   numbers_end = remove_if(numbers.get(), numbers_end,
      [](auto x) {return x >= 1000; });
   cout << "Numbers less than 1000:";
   for_each(numbers.get(), numbers_end, [](auto x) { cout << " " << x ; });
   cout << endl;

   // Of the numbers less than 1000, find all odd numbers 
   numbers_end = remove_if(numbers.get(), numbers_end,
      [](auto x) { return (x % 2) == 0; });
   cout << "Odd numbers:";
   for (int i = 0; i < numbers_end - numbers.get(); i++) {
      cout << " " << numbers[i];
   }
   cout << endl;


   // Get 5 more numbers
   count = 5;
   unique_ptr<int[]> numbers2(new int[count]);
   cout << endl;
   cout << "Enter 5 more numbers: " << endl;
   for (int i = 0; i < count; i++) {
      cout << "Number " << i + 1 << ": ";
      cin >> numbers2[i];
   }

   // what if you accidentally pass in count+1 instead of count?
   sum = calc_sum(count, numbers2);
   average = (float)sum / count;
   min = find_min(count, numbers2);
   max = find_max(count, numbers2);

   cout << endl;
   cout << "Sum: " << sum << endl;
   cout << "Average: " << average << endl;
   cout << "Minimum: " << min << endl;
   cout << "Maximum: " << max << endl;
   return 0;
}

int calc_sum(int count, const unique_ptr<int[]>& numbers)
{
   int sum = 0;

   // what if you mistakenly use <= instead of < here?
   for (int i = 0; i < count; i++) {  
      sum += numbers[i];
   }
   return sum;
}

int find_min(int count, const unique_ptr<int[]>& numbers)
{
   int min = numbers[0];
   for (int i = 1; i < count; i++) {
      min = (numbers[i] < min) ? numbers[i] : min;
   }
   return min;
}

int find_max(int count, const unique_ptr<int[]>& numbers)
{
   int max = numbers[0];
   for (int i = 1; i < count; i++) {
      max = (numbers[i] > max) ? numbers[i] : max;
   }
   return max;
}
