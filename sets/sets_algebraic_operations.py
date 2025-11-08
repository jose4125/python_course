dark_hair = {'juan', 'karla', 'pedro', 'maria'}
blond_hair = {'lorenzo', 'laura', 'marco'}
brown_eyes = {'karla', 'laura'}
under_30 = {'juan', 'karla', 'maria'}

# union - all persons with brown eyes or blond hair or both
# Union: combines all elements from both sets (like “OR”).
# is Commutative - Commutative means the order of the operands doesn’t change the result.
print(f'brown eyes and blond hair (union): {brown_eyes.union(blond_hair)}')

# union with pipe ( | ) operator
print(f'brown eyes and blond hair (union): {brown_eyes | blond_hair}')


# intersection - only persons with brown eyes and blond hair
# Intersection: keeps only the elements found in both sets (like “AND”).
# is Commutative - Commutative means the order of the operands doesn’t change the result.
print(f'brown eyes and blond hair (intersection): {brown_eyes.intersection(blond_hair)}')

# intersection with ( & ) operator
print(f'brown eyes and blond hair (intersection): {brown_eyes & blond_hair}')


# difference - only persons with dark hair with no brown eyes
# Difference: keeps elements that are in the first set but not in the second.
# is not Commutative - not Commutative means the order of the operands change the result.
print(f'dark hair with no brown eyes (difference): {dark_hair.difference(brown_eyes)}')

# difference with minus ( - ) operator
print(f'dark hair with no brown eyes (difference): {dark_hair - brown_eyes}')


# symmetric difference - only persons with dark hair or brown eyes but not both
# Symmetric difference: keeps elements that are in one set or the other, but not in both.
# is Commutative - Commutative means the order of the operands doesn’t change the result.
print(f'dark hair or brown eyes but not both (symmetric difference): {dark_hair.symmetric_difference(brown_eyes)}')

# symmetric difference with ( ^ ) operator
print(f'dark hair or brown eyes but not both (symmetric difference): {dark_hair ^ brown_eyes}')

