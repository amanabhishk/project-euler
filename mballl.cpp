#include<stdio.h>
// #include<math.h>
using namespace std;

int main()
{
	int l;
	scanf("%d",&l);
	

	// l = 1;
	

	unsigned long long int a[100001]={0},copy[100001]={0};
	for (int k=0;k<100001;k += 2) {a[k] = 1;copy[k] = 1;}


	a[0]++;
	copy[0]++;
	for(int f = 3;f<100001;f ++) {a[f] = copy[f] + a[f-3];}


	for (int k=0;k<100001;k ++) {copy[k] = a[k];}
	a[0]++;
	copy[0]++;
	for(int t = 6;t<100001;t++) {a[t] = copy[t] + a[t-6];}


	for (int k=0;k<100001;k ++) {copy[k] = a[k];}
	// a[0]++;
	// copy[0]++;
	for(int t = 7;t<100001;t++) {a[t] = copy[t] + a[t-7];}


	for (int k=0;k<100001;k ++) {copy[k] = a[k];}
	// a[0]++;
	// copy[0]++;
	for(int t = 8;t<100001;t++) {a[t] = copy[t] + a[t-8];}



	while (l--)
	{
		int input = 10;
		scanf("%d",&input);
		printf("%llu\n", a[input]);;

		

	}

	return 0;
}


