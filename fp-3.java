import java.util.*;
import java.lang.*;
import java.util.ArrayList;

class Rextester {
    static Integer d;

    static class MutableCmp implements Comparator<Integer> {
        @Override
        public int compare(Integer a, Integer b) { return a%d - b%d; }
    }

    static class ImmutableCmp implements Comparator<Integer> {
        Integer d;

        ImmutableCmp(Integer d) { this.d = d; }

        @Override
        public int compare(Integer a, Integer b) { return a%this.d - b%this.d; }
    }

    public static void main(String args[]) {
        ArrayList<Integer> a = new ArrayList<>();
        for (int i=0; i<10; i++) a.add(i);

        Scanner scan = new Scanner(System.in);

        MutableCmp mc = new MutableCmp();

        while (scan.hasNextInt()) {
            int i = scan.nextInt();

            d = i;
            Collections.sort(a, mc);
            System.out.println(a);

            Collections.sort(a, new ImmutableCmp(i));
            System.out.println(a);

            System.out.println();
        }
    }
}

/*
# Python

def addGen(x):
    def go(y): return x+y
    return go

add1 = addGen(1)
add3 = addGen(3)

print (add1(1))
print (addGen(1)(1))
print (add3(1))
*/
