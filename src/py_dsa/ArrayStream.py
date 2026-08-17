from functools import reduce

def main():
    # Sample data
    names = [
        "Reflection", "Collection", "Stream",
        "Structure", "Sorting", "State"
    ]

    # forEach: Print each name
    print("forEach:")
    for name in names:
        print(name)

    # collect: Collect names starting with 'S' into a list
    s_names = [name for name in names if name.startswith("S")]
    print("\ncollect (names starting with 'S'):")
    for name in s_names:
        print(name)

    # reduce: Concatenate all names into a single string
    concatenated_names = reduce(lambda acc, e: acc + " " + e, names, "").strip()
    print("\nreduce (concatenated names):")
    print(concatenated_names)

    # count: Count the number of names
    count = len(names)
    print("\ncount:")
    print(count)

    # findFirst: Find the first name
    first_name = names[0] if names else None
    print("\nfindFirst:")
    if first_name:
        print(first_name)

    # allMatch: Check if all names start with 'S'
    all_start_with_s = all(name.startswith("S") for name in names)
    print("\nallMatch (all start with 'S'):")
    print(all_start_with_s)

    # anyMatch: Check if any name starts with 'S'
    any_start_with_s = any(name.startswith("S") for name in names)
    print("\nanyMatch (any start with 'S'):")
    print(any_start_with_s)


if __name__ == "__main__":
    main()


# import java.util.*;
# import java.util.stream.Collectors;
#
# public class StreamTerminalOperationsExample {
#     public static void main(String[] args) {
#         // Sample data
#         List<String> names = Arrays.asList(
#             "Reflection", "Collection", "Stream",
#             "Structure", "Sorting", "State"
#         );
#
#         // forEach: Print each name
#         System.out.println("forEach:");
#         names.stream().forEach(System.out::println);
#
#         // collect: Collect names starting with 'S' into a list
#         List<String> sNames = names.stream()
#                                    .filter(name -> name.startsWith("S"))
#                                    .collect(Collectors.toList());
#         System.out.println("\ncollect (names starting with 'S'):");
#         sNames.forEach(System.out::println);
#
#         // reduce: Concatenate all names into a single string
#         String concatenatedNames = names.stream().reduce(
#             "",
#             (partialString, element) -> partialString + " " + element
#         );
#         System.out.println("\nreduce (concatenated names):");
#         System.out.println(concatenatedNames.trim());
#
#         // count: Count the number of names
#         long count = names.stream().count();
#         System.out.println("\ncount:");
#         System.out.println(count);
#
#         // findFirst: Find the first name
#         Optional<String> firstName = names.stream().findFirst();
#         System.out.println("\nfindFirst:");
#         firstName.ifPresent(System.out::println);
#
#         // allMatch: Check if all names start with 'S'
#         boolean allStartWithS = names.stream().allMatch(
#             name -> name.startsWith("S")
#         );
#         System.out.println("\nallMatch (all start with 'S'):");
#         System.out.println(allStartWithS);
#
#         // anyMatch: Check if any name starts with 'S'
#         boolean anyStartWithS = names.stream().anyMatch(
#             name -> name.startsWith("S")
#         );
#         System.out.println("\nanyMatch (any start with 'S'):");
#         System.out.println(anyStartWithS);
#
#     }
# }
##

