
def findMean(A, N):

    if (N == 1):
        return (float)
        # A[N - 1]
    else:
        return ((float)(findMean(A, N - 1) * (N - 1) +
                    A[N - 1]) / N)

def main():

    Mean = 0

    A = {1, 2, 3, 4, 5}
    for a in A:
        N = a/ len(A)
        print("%.2f\n", findMean(A, N))
    # return 0

