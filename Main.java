import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Employee {
    private String id;
    private String name;
    private boolean isPresent;

    public Employee(String id, String name) {
        this.id = id;
        this.name = name;
        this.isPresent = false;
    }

    public String getId() { return id; }
    public String getName() { return name; }
    public boolean isPresent() { return isPresent; }
    public void setPresent(boolean present) { isPresent = present; }
}

class AttendanceManagementSystem {
    private Map<String, Employee> employees = new HashMap<>();

    // Register an employee in the system
    public void registerEmployee(String id, String name) {
        Employee employee = new Employee(id, name);
        employees.put(id, employee);
        System.out.println("Employee " + name + " registered successfully.");
    }

    // Mark attendance for an employee
    public void markAttendance(String id) {
        Employee employee = employees.get(id);
        if (employee != null) {
            employee.setPresent(true);
            System.out.println("Attendance marked for " + employee.getName());
        } else {
            System.out.println("Employee not found.");
        }
    }

    // Generate attendance report
    public void generateReport() {
        System.out.println("Attendance Report:");
        for (Employee employee : employees.values()) {
            String status = employee.isPresent() ? "Present" : "Absent";
            System.out.println(employee.getName() + " (" + employee.getId() + "): " + status);
        }
    }

    // Reset attendance status at the end of the day
    public void resetAttendance() {
        for (Employee employee : employees.values()) {
            employee.setPresent(false);
        }
        System.out.println("Attendance has been reset for the next day.");
    }
}

public class Main {
    public static void main(String[] args) {
        AttendanceManagementSystem system = new AttendanceManagementSystem();
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        // Sample loop for user operations
        while (running) {
            System.out.println("\nAttendance Management System:");
            System.out.println("1. Register Employee");
            System.out.println("2. Mark Attendance");
            System.out.println("3. Generate Attendance Report");
            System.out.println("4. Reset Attendance");
            System.out.println("5. Exit");

            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter Employee ID: ");
                    String id = scanner.nextLine();
                    System.out.print("Enter Employee Name: ");
                    String name = scanner.nextLine();
                    system.registerEmployee(id, name);
                    break;
                case 2:
                    System.out.print("Enter Employee ID: ");
                    id = scanner.nextLine();
                    system.markAttendance(id);
                    break;
                case 3:
                    system.generateReport();
                    break;
                case 4:
                    system.resetAttendance();
                    break;
                case 5:
                    running = false;
                    System.out.println("Exiting the system.");
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
            }
        }
        scanner.close();
    }
}
