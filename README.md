## Cima API

### API Reference
test

#### Calibers 
List all calibers
```/api/v1/calibers```

Query Params:
 - species_id *Required* Integer
 - variety_id *Optional* Integer
 - category_id *Optional* Integer
 - packaging_id *Optional* Integer


#### Categories
List all categories
```/api/v1/categories```

Query Params:
 - species_id *Required* Integer
 - variety_id *Optional* Integer


#### Markets
List all markets
```/api/v1/markets```

Query Params:
 - species_id   *Required* Integer
 - variety_id   *Optional* Integer
 - category_id  *Optional* Integer
 - packaging_id *Optional* Integer
 - caliber_id *Optional* Integer
 - region_id    *Optional* Integer

#### Groups
List all groups
```/api/v1/groups```

#### Packaging
List all packaging
```/api/v1/packaging```

Query Params:
 - species_id *Required* Integer
 - variety_id *Optional* Integer
 - category_id *Optional* Integer
 - packaging_id *Optional* Integer 

#### Regions
List all regions for 
```/api/v1/regions```

Query Params:
 - species_id   *Required* Integer
 - variety_id   *Optional* Integer
 - category_id  *Optional* Integer
 - packaging_id *Optional* Integer
 - caliber_id *Optional* Integer


#### Species
List all species for 
```/api/v1/species/<group_id>```


#### Varieties
List all varieties for 
```/api/v1/varieties/<species_id>```