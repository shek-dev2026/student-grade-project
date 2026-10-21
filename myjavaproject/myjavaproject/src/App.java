import java.util.Scanner;

public class App {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter student name: ");
        String name = sc.nextLine();

        System.out.print("Enter department: ");
        String department = sc.nextLine();

        System.out.print("Enter semester: ");
        int semester = sc.nextInt();

        int total = 0;

        for (int i = 1; i <= 5; i++) {
            System.out.print("Enter subject " + i + " marks: ");
            int marks = sc.nextInt();
            total += marks;
        }

        double percentage = total / 5.0;

        System.out.println("\n===== STUDENT RESULT =====");
        System.out.println("Name: " + name);
        System.out.println("Department: " + department);
        System.out.println("Semester: " + semester);
        System.out.println("Total Marks: " + total + "/500");
        System.out.println("Percentage: " + percentage + "%");

        if (percentage >= 90)
            System.out.println("Grade: S");
        else if (percentage >= 80)
            System.out.println("Grade: A");
        else if (percentage >= 65)
            System.out.println("Grade: B");
        else if (percentage >= 50)
            System.out.println("Grade: C");
        else
            System.out.println("Grade: Fail");

        sc.close();
    }
}