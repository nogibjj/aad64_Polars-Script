from main import avg_88
import polars as pl

dataset = {"Values": [1, 3, 5, 7, 9]}
testing_data = pl.DataFrame(dataset)
def testing_main():
    assert avg_88(testing_data['Values']) == 5
    print("the mean is 5")
    
testing_main()