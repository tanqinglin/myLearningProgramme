
import java.util.*;

public class Exercise {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please input your name:");
        String name = scanner.nextLine();
        System.out.println("Please input your age:");
        int age = scanner.nextInt();
        System.out.printf("Hi, %s, you are %d years old.", name, age);

        scanner = new Scanner(System.in);
        System.out.println("Please input your score last time:");
        float score1 = scanner.nextInt();
        System.out.println("Please input your score this time:");
        float score2 = scanner.nextInt();
        System.out.printf("Xiaoming has promoted himself %.2f%%", (score2 - score1) / score1);
    
        String fruit = "apple";
        switch (fruit) {
            case "apple" -> System.out.println("Selected apple");
            case "pear" -> System.out.println("Selected pear");
            case "mango" -> {
                System.out.println("Selected mango");
                System.out.println("Good choice!");
            } // 新语法使用 `->` 而不是 `:` ，且需不要 `break`
            default -> System.out.println("No fruit selected");
        }
        
        int[] ns = {1, 3, 7, 11, 12, 15};
        System.out.println(Arrays.toString(ns));
    
    }
}