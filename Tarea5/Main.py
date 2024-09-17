import LinearSearch
import SentinelLinealSearch
import BinarySearch

def searchResult(search):
    if search == -1:
        print("No se encontró")
    else:
        print("El valor se encuentra en: ",search)

alpha = [0,1,2,3,4]
beta = [5,6,7]

searchResult(LinearSearch.linearSearch(alpha,6))
searchResult(LinearSearch.linearSearch(beta,6))
searchResult(SentinelLinealSearch.sentinelLinearSearch(alpha,7))
searchResult(SentinelLinealSearch.sentinelLinearSearch(beta,7))
searchResult(BinarySearch.binarySearch(alpha,5))
searchResult(BinarySearch.binarySearch(beta,5))