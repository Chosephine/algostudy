/*
 * programmers 코딩테스트 입문
 * 배열의 평균값
*/

public class solve011{
	
	public static double solution(int[] numbers) {
		int N = numbers.length;
		// sum이 int일 경우 올바른 출력 X
        double sum = 0;
        for (int num : numbers) {
        	sum += num;
        }
        double answer = sum / N;
        return answer;
    }

    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
    	int[] numbers = {89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99};
//    	int people = 12;
    	double answer = solution(numbers);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(answer);
//    	System.out.println(answer);
    }
}
