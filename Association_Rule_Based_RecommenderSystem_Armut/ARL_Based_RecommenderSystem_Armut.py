# region read & import

# !pip install mlxtend

import pandas as pd
import datetime
import warnings
from mlxtend.frequent_patterns import apriori, association_rules

warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv("Recommendation_Systems/CaseStudy/Association_Rule_Based_RecommenderSystem_Armut/dataset/armut_data.csv")
df.head()

# endregion

# region ServiceId_CategoryId with join method
Service_Category = df[["ServiceId", "CategoryId"]]
Service_Category.values
df["Serv_Cat_Ids"] = ["_".join(col) for col in Service_Category.astype(str).values]

df.head()
# endregion

# region Creating Shopping_Date -- 1st Way

df["CreateDate"] = pd.to_datetime(df["CreateDate"])
df["CreateDate"].dtype
df["Shopping_Date"] = df["CreateDate"].dt.to_period('M')

df.head()
# endregion

# region Creating Shopping_Date -- 2nd Way

# df["month"] = pd.DatetimeIndex(df["CreateDate"]).month
# df["year"] = pd.DatetimeIndex(df["CreateDate"]).year

# month_year = df[["month", "year"]]

# df["Shopping_Date"] = ["_".join(col) for col in month_year.astype(str).values]

# df.head()

# endregion

# region Creating Shopping_Date -- 3rd Way
# df["CreateDate"] = pd.to_datetime(df["CreateDate"])
# df["CreateDate"].dtype

# df["month"] = df["CreateDate"].dt.month
# df["year"] = df["CreateDate"].dt.year

# month_year = df[["month", "year"]]
# df["CreateDate"] = ["_".join(col) for col in month_year.astype(str).values]
# df.head()

# endregion

# region Creating BoxID

user_date = df[["UserId", "Shopping_Date"]]
df["BoxID"] = ["_".join(col) for col in user_date.astype(str).values]
df.head()

# endregion

# region Creating InvoiceID-Serv_Cat_Ids pivot table

arl_df = df.pivot_table("UserId", "BoxID", "Serv_Cat_Ids", aggfunc="count", fill_value="0").astype(float) \
    .applymap(lambda x: 1 if x != 0 else 0)

# endregion

# region Creating Association Rules

frequent_itemsets = apriori(arl_df, min_support=0.01, use_colnames=True)
frequent_itemsets.sort_values('support', ascending=False)

rules = association_rules(frequent_itemsets, metric="support", min_threshold=0.01)
rules.sort_values("lift", ascending=False)

# endregion

# region Creating arl_recommender Function


def arl_recommender(rules_df, product_id, rec_count=1):
    sorted_rules = rules_df.sort_values("lift", ascending=False)
    recommendation_list = []
    for i, product in enumerate(sorted_rules["antecedents"]):
        for j in list(product):
            if j == product_id:
                recommendation_list.append(list(sorted_rules.iloc[i]["consequents"])[0])

    return recommendation_list[0: rec_count]

# endregion

# region Recommending a service to a user whose last receive is 2_0 service with arl_recommender function

arl_recommender(rules, "2_0", 1)
arl_recommender(rules, "2_0", 2)
arl_recommender(rules, "2_0", 3)

# endregion