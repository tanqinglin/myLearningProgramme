#include "uthash.h"

struct number_hash {
  int value;
  int index;
  UT_hash_handle hh;
};

void destroy_table(struct number_hash** table) {
  struct number_hash* curr;
  struct number_hash* tmp;
  
  HASH_ITER(hh, *table, curr, tmp) {
    HASH_DEL(*table, curr);
    free(curr);
  }
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
  struct number_hash* table = NULL;
  struct number_hash* element;
  int* ret = (int*) malloc(2 * sizeof(int));
  int remaining;
  for (int i = 0; i < numsSize; ++i) {
    remaining = target - nums[i];
   
    // Find if there has already been an element such that the sum is target
    HASH_FIND_INT(table, &remaining, element);
    if (element) {
      ret[0] = element->index;
      ret[1] = i;
      break;
    }
   
    // Add the new number to the hash table if it doesn't exist already
    HASH_FIND_INT(table, &nums[i], element);
    if (!element) {
      element = (struct number_hash *) malloc(sizeof(*element));
      element->value = nums[i];
      element->index = i;

      HASH_ADD_INT(table, value, element);
    }
  }
  
  destroy_table(&table);
  
  *returnSize = 2;
  return ret;
}