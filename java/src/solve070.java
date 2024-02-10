import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Set;

/*
 * 백준 1181 단어 정렬 
 * https://www.acmicpc.net/problem/1181
 * */

public class solve070 {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		Set<String> words = new HashSet<>();
		
		for (int i = 0; i < N ; i ++) {
			words.add(br.readLine());
		}

		ArrayList<String> wordsArr = new ArrayList<>(words);
		Collections.sort(wordsArr, new Comparator<String>() {
			
			@Override
			public int compare(String s1, String s2) {
				int compareLength = s1.length() - s2.length();
				if (compareLength != 0) {
					return compareLength;
				} else {
					return s1.compareTo(s2);
				}
			}
		
		});
		
		for (String word : wordsArr) {
			System.out.println(word);
		}

		
	}
}
