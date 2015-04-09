#include<stdio.h>
#include<string.h>
using namespace std;

int multi(long long a, long long b);

int main()
{
	unsigned long long t1 = 19002374980,t2=23209842;
	// printf("%lld\n",t);
	multi(t1,t2);
	return 0;
}

int multi(long long A, long long B)
{
	// sizes of two numbers
	long long a = A, b = B;
	unsigned int lena = 0, lenb = 0;
	
	while (a>9)
	{
		lena ++;
		a = (a-a%10)/10;
	} 
	lena ++;
	while (b>9)
	{
		lenb++;
		b = (b-b%10)/10;
	} 
	lenb++;
	
	//converting into array 
	int ar[lena],br[lenb];
	int i = 0, j = 0;
	while (i < lena)
	{
		ar[i] = A%10;
		A = (A-A%10)/10;
		i++;
	} 

	while (j < lenb)
	{
		br[j] = B%10;
		B = (B-B%10)/10;
		j++;
	} 


	// long multiplication
	i = 0,j=0;
	if(lena>lenb) int row[lenb][lena+lenb] = {{0}};
	else int row[lena][lena+lenb] = {{0}};
	
	while (i<lena)
	{
		while (j<lenb)
		{
			row[i] = 
	}








	printf("%d %d -- %d %d",ar[0],ar[1],ar[9],ar[10]);




	return lena;
}