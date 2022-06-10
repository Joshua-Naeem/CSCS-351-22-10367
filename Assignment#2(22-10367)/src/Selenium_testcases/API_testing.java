package Selenium_testcases;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class API_testing {

	public static void main(String[] args) {
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\hp\\Downloads\\Selenium\\EXE\\chrome\\chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		
		String e = "joshua@gmail.com";
		String p = "123456";
			
		
		driver.get("http://www.facebook.com/");
		driver.findElement(By.id("email")).sendKeys(e);
		driver.findElement(By.id("pass")).sendKeys(p);
		driver.findElement(By.name("login")).click();
		
		//Strings for test case 1
		String at = driver.getTitle();
		String et = "Facebook – log in or sign up";
		
		
		
		driver.close();
	
		//Test Case (Returns the name of the Web Page!)
		if(at.equalsIgnoreCase(et)){
			
			System.out.println("Test Success");
		}
		else {
			System.out.println("Test Failure");
		}

	}

}
