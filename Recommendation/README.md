# Recommender
## Usage
***recommendation_system*.*Recomemder(*dataset*)***

```
from recommendation_system import Recommender

# given a dataset
dataset = [['itemC', 'itemB', 'itemE'],
           ['itemE', 'itemG','itemA','itemB', 'itemD'，...],
           ...]

# new a Recommender object        
rs = Recommender(dataset)

# recommend user 0 5 items accroding to the most popular
popular = rs.popular(dataset[0], n=5)

# recommend user 0 5 items accroding to the user-based CF
user_based = rs.user_based(0)[:5]

# recommend user 0 some items accroding to the item-based CF
item_based = rs.item_based(0)
```

## Parameter
dataset:
> list of list

## Attributes
dataset
> list of list, the inner list is the items which a user interests  

unique
> the union of all items 

usr_matrix
> the similarity matrix of user to user

item_matrix
> the similarity matrix of item to item

## Methods

popular(data, n=None)
> recommend items according to the most popular
>
> parameter
>> data: []
>>
>> n: number of recommending items
>
> return
>> tuple of list

user_based(subset, include_current_items=False)
> recommend items according to user-based collaborative filtering
>
> parameter
>> subset: int, the index of dataset
>>
>> include_current_items: bool
>
> return
>> tuple of list

item_based(subset, include_current_items=False)
> recommend items according to item-based collaborative filtering 
>
> parameter
>> subset: int, the index of dataset
>>
>> include_current_items: bool
>
> return
>> tuple of list

most_similar_set_to(subset)
> recommend items to 
>
> parameter
>> subset: int, index of dataset 
>
> return
>> tuple of list, [(subset_i, similarity), ...]

most_similar_item_to(item_id)
> recommend items to 
>
> parameter
>> item_id: int, index of item
>
> return
>> tuple of list, [(item_i, similarity), ...]