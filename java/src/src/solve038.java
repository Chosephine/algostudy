package src;

/*
 * 팩토리얼 
*/

public class solve038 {
	 public static int solution(int n) {
		 int answer = 0;
	        for (int i=1; i<=10; i++){
	            int mul = 1;
	            for (int j=1; j<=i; j++){
	                mul *= j;
	                if (mul > n) {
	                    answer = i-1;
	                    break;
	                } else if (mul == n){
	                    answer = i;
	                    break;
	                }
	            }
	            if (answer > 0) break;
	        }
	        return answer;
	    }
	
	public static void main(String[] args) {
		int n = 3628800;
		int answer = solution(n);
		System.out.println(answer);
	}
}
