public class Algorithms_005_Find_All_Permutations {

    private static void permutationsInOrder(String s) {
        permutationsInOrder("", s);
    }

    private static void permutationsInOrder(String prefix, String s) {
        int n = s.length();
        if (n == 0) {
            System.out.println(prefix);
        }
        for (int i = 0; i < n; i++) {
            permutationsInOrder(prefix + s.charAt(i), s.substring(0, i) + s.substring(i + 1, n));
        }
    }

    private static void permutationsWithoutOrder(String s) {
        int n = s.length();
        char[] a = new char[n];
        for (int i = 0; i < n; i++) {
            a[i] = s.charAt(i);
        }
        permutationsWithoutOrder(a, n);
    }

    private static void permutationsWithoutOrder(char[] s, int n) {
        if (n == 1) {
            System.out.println(new String(s));
        }
        for (int i = 0; i < n; i++) {
            swap(s, i, n - 1);
            permutationsWithoutOrder(s, n - 1);
            swap(s, i, n - 1);
        }
    }

    private static void swap(char[] a, int i, int j) {
        char c = a[i];
        a[i] = a[j];
        a[j] = c;
    }

    public static void main(String[] args) {
        System.out.println("** Permutation with order ***");
        permutationsInOrder("abc");
        System.out.println("** Permutation w/o order  ***");
        permutationsWithoutOrder("rope");
    }
}
