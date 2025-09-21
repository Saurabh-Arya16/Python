#program to do the set operation -> union,intersection,difference,symmetric_difference

utensils={"fork","spoon","Knife"}
dishes={"bowl","plate","cup","Knife"}

print("\nBy Operator method")

print(f"Union={utensils | dishes}")
print(f"Intersection={utensils & dishes}")
print(f"difference={utensils - dishes}")
print(f"symmetric_difference={utensils^dishes}")

print("\n by function method")

print(f"union={utensils.union(dishes)}")
print(f"Intersection={utensils.intersection(dishes)}")
print(f"difference={utensils.difference(dishes)}")
print(f"symmetric_difference={utensils.symmetric_difference(dishes)}")