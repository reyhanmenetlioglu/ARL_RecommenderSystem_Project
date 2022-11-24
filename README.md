##### ARL Based Recommender System using the Armut Data
 
##### Business Problem : 
Armut, Turkey's largest online service platform, brings together service providers and those who want to receive service. It provides easy access to services such as cleaning, modification and transportation with a few touches on the computer or smart phone. It is desired to create a product recommendation system with Association Rule Learning by using the data set containing the service users and the services and categories these users have received.

  
| Variables          | Meaning                                                                                                   |
|-------------------:|-----------------------------------------------------------------------------------------------------------|
|          UserId    | Customer number                                                                                           |
|          ServiceId | Anonymized services belonging to each category(Exp:Upholstery washing service under the cleaning category)|
|          CategoryId| Anonymized categories(Exp:Cleaning, transportation, renovation category)                                  |
|          CreateDate| The date the service was purchased                                                                        |

Note : A ServiceId can be found under different categories and refers to different services under different categories. (Example: The service with CategoryId 7 and ServiceId 4 is honeycomb cleaning, while the service with CategoryId 2 and ServiceId 4 is furniture assembly)
