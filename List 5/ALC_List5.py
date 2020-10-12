from importlib.machinery import SourceFileLoader
import math

Matrix_Utils = SourceFileLoader("Matrix_Utils", "/home/bdantas/Área de Trabalho/ALC_Lists/Utils/Matrix_Utils.py").load_module()
ALC_List1    = SourceFileLoader("ALC_List1", "/home/bdantas/Área de Trabalho/ALC_Lists/List_1/ALC_List1.py").load_module()


Weight_Legendre = {2:{"points": [-0.5773502691896257,0.5773502691896257],"weight": [1.0,1.0]},
                   3:{"points": [0.0,-0.7745966692414834,0.7745966692414834],"weight": [0.8888888888888888,0.5555555555555556,0.5555555555555556]},
                   4:{"points": [-0.3399810435848563,0.3399810435848563,-0.8611363115940526,0.8611363115940526],"weight": [0.6521451548625461,0.6521451548625461,0.3478548451374538,0.3478548451374538]},
                   5:{"points": [0.0,-0.5384693101056831,0.5384693101056831,-0.9061798459386640,0.9061798459386640],"weight": [0.5688888888888889,0.4786286704993665,0.4786286704993665,0.2369268850561891,0.2369268850561891]},
                   6:{"points": [0.6612093864662645,-0.6612093864662645,-0.2386191860831969,0.2386191860831969,-0.9324695142031521,0.9324695142031521],"weight": [0.3607615730481386,0.3607615730481386,0.4679139345726910,0.4679139345726910,0.1713244923791704,0.1713244923791704]},
                   7:{"points": [0.0,0.4058451513773972,-0.4058451513773972,-0.7415311855993945,0.7415311855993945,-0.9491079123427585,0.9491079123427585],"weight": [0.4179591836734694,0.3818300505051189,0.3818300505051189,0.2797053914892766,0.2797053914892766,0.1294849661688697,0.1294849661688697]},
                   8:{"points": [-0.1834346424956498,0.1834346424956498,-0.5255324099163290,0.5255324099163290,-0.7966664774136267,0.7966664774136267,-0.9602898564975363,0.9602898564975363],"weight": [0.3626837833783620,0.3626837833783620,0.3137066458778873,0.3137066458778873,0.2223810344533745,0.2223810344533745,0.1012285362903763,0.1012285362903763]},
                   9:{"points": [0.0,-0.8360311073266358,0.8360311073266358,-0.9681602395076261,0.9681602395076261,-0.3242534234038089,0.3242534234038089,-0.6133714327005904,0.6133714327005904],"weight": [0.3302393550012598,0.1806481606948574,0.1806481606948574,0.0812743883615744,0.0812743883615744,0.3123470770400029,0.3123470770400029,0.2606106964029354,0.2606106964029354]},
                   10:{"points": [-0.1488743389816312,0.1488743389816312,-0.4333953941292472,0.4333953941292472,-0.6794095682990244,0.6794095682990244,-0.8650633666889845,0.8650633666889845,-0.9739065285171717,0.9739065285171717],"weight": [0.2955242247147529,0.2955242247147529,0.2692667193099963,0.2692667193099963,0.2190863625159820,0.2190863625159820,0.1494513491505806,0.1494513491505806,0.0666713443086881,0.0666713443086881]}}

Weight_Hermite = {2:{"points": [-0.7071067811865475244008,0.7071067811865475244008],"weight": [0.8862269254527580136491,0.8862269254527580136491]},
                  3:{"points": [-1.224744871391589049099,0.0,1.224744871391589049099],"weight": [0.295408975150919337883,1.181635900603677351532,0.295408975150919337883]},
                  4:{"points": [-1.650680123885784555883,-0.5246476232752903178841,0.5246476232752903178841,1.650680123885784555883],"weight": [0.081312835447245177143,0.8049140900055128365061,0.8049140900055128365061,0.08131283544724517714303]},
                  5:{"points": [-2.020182870456085632929,-0.9585724646138185071128,0.0,0.9585724646138185071128,2.020182870456085632929],"weight": [0.01995324205904591320774,0.3936193231522411598285,0.9453087204829418812257,0.393619323152241159828,0.01995324205904591320774]},
                  6:{"points": [-2.350604973674492222834,-1.335849074013696949715,-0.4360774119276165086792,0.436077411927616508679,1.335849074013696949715,2.350604973674492222834],"weight": [0.004530009905508845640857,0.1570673203228566439163,0.7246295952243925240919,0.724629595224392524092,0.1570673203228566439163,0.004530009905508845640857]},
                  7:{"points": [-2.350604973674492222834,-1.335849074013696949715,-0.4360774119276165086792,0.436077411927616508679,1.335849074013696949715,2.350604973674492222834],"weight": [0.004530009905508845640857,0.1570673203228566439163,0.7246295952243925240919,0.724629595224392524092,0.1570673203228566439163,0.004530009905508845640857]},
                  8:{"points": [-2.930637420257244019224,-1.981656756695842925855,-1.157193712446780194721,-0.3811869902073221168547,0.3811869902073221168547,1.157193712446780194721,1.981656756695842925855,2.930637420257244019224],"weight": [1.99604072211367619206E-4,0.0170779830074134754562,0.2078023258148918795433,0.6611470125582412910304,0.6611470125582412910304,0.2078023258148918795433,0.0170779830074134754562,1.996040722113676192061E-4]},
                  9:{"points": [-3.19099320178152760723,-2.266580584531843111802,-1.468553289216667931667,-0.7235510187528375733226,0.0,0.7235510187528375733226,1.468553289216667931667,2.266580584531843111802,3.19099320178152760723],"weight": [3.960697726326438190459E-5,0.00494362427553694721722,0.088474527394376573288,0.4326515590025557501998,0.7202352156060509571243,0.4326515590025557502,0.088474527394376573288,0.004943624275536947217225,3.96069772632643819046E-5]},
                  10:{"points": [-3.436159118837737603327,-2.532731674232789796409,-1.756683649299881773451,-1.036610829789513654178,-0.3429013272237046087892,0.3429013272237046087892,1.036610829789513654178,1.756683649299881773451,2.532731674232789796409,3.436159118837737603327],"weight": [7.64043285523262062916E-6,0.001343645746781,0.03387439445548,0.2401386110823146864165,0.61086263373257987836,0.6108263373532,0.24013861108,0.033874394455481,0.00134364574812326,7.64043285523262062916E-6]}}

Weight_Laguerre = {2:{"points": [0.5857864376269049511983,3.414213562373095048802],"weight": [0.8535533905932737622004,0.1464466094067262377996]},
                   3:{"points": [0.4157745567834790833115,2.29428036027904171982,6.289945082937479196866],"weight": [0.71109300992917301545,0.2785177335692408488014,0.01038925650158613574897]},
                   4:{"points": [0.3225476896193923118004,1.745761101158346575687,4.536620296921127983279,9.395070912301133129234],"weight": [0.603154104341633601636,0.3574186924377996866415,0.03888790851500538427244,5.392947055613274501038E-4]},
                   5:{"points": [0.2635603197181409102031,1.413403059106516792218,3.596425771040722081223,7.085810005858837556922,12.64080084427578265943],"weight": [0.5217556105828086524759,0.3986668110831759274541,0.0759424496817075953877,0.00361175867992204845446,2.33699723857762278911E-5]},
                   6:{"points": [0.2228466041792606894644,1.188932101672623030743,2.992736326059314077691,5.77514356910451050184,9.837467418382589917716,15.98287398060170178255],"weight": [0.4589646739499635935683,0.417000830772120994113,0.113373382074044975739,0.01039919745314907489891,2.610172028149320594792E-4,8.9854790642962123883E-7]},
                   7:{"points": [0.1930436765603624138383,1.026664895339191950345,2.567876744950746206908,4.900353084526484568102,8.182153444562860791082,12.73418029179781375801,19.39572786226254031171],"weight": [0.4093189517012739021304,0.4218312778617197799293,0.1471263486575052783954,0.02063351446871693986571,0.001074010143280745522132,1.586546434856420126873E-5,3.17031547899558056227E-8]},
                   8:{"points": [3.17031547899558056227E-8,0.903701776799379912186,2.25108662986613068931,4.266700170287658793649,7.045905402393465697279,10.75851601018099522406,15.74067864127800457803,22.8631317368892641057],"weight": [0.369188589341637529921,0.418786780814342956077,0.1757949866371718056997,0.03334349226121565152213,0.00279453623522567252494,9.07650877335821310424E-5,8.48574671627253154487E-7,1.04800117487151038162E-9]},
                   9:{"points": [0.152322227731808247428,0.8072200227422558477414,2.005135155619347122983,3.783473973331232991675,6.204956777876612606974,9.37298525168757620181,13.4662369110920935711,18.83359778899169661415,26.37407189092737679614],"weight": [0.3361264217979625196735,0.4112139804239843873091,0.1992875253708855808606,0.0474605627656515992621,0.005599626610794583177004,3.05249767093210566305E-4,6.59212302607535239226E-6,4.1107693303495484429E-8,3.29087403035070757647E-11]},
                   10:{"points": [0.1377934705404924308308,0.72945454950317049816,1.8083429017,3.40143369785,5.552496,8.330152746,11.843785837900,16.27925783137810209953,21.99658581198076195128,29.92069701227389155991],"weight": [0.3084411157650201415475,0.401119929155273551516,0.2180682876118094215886,0.0620874560986777473929,0.00950151697518110055384,7.53008388587538775456E-4,2.82592334959956556742E-5,4.24931398496268637259E-7,1.839564823979630780922E-9,9.911827219609008558378E-13]}}

def integrate(function, a, b, number_of_points, polinomial_integration = True):
    def laguerre_function(x):
        return function(x)/(math.exp(-x))

    def hermite_function(x):
        return function(x)/(math.exp(-x**2))

    weight_hermite   = Weight_Hermite.get(number_of_points).get("weight")
    points_hermite   = Weight_Hermite.get(number_of_points).get("points")
    weight_laguerre  = Weight_Laguerre.get(number_of_points).get("weight")
    points_laguerre  = Weight_Laguerre.get(number_of_points).get("points")
    hermite_sum      = 0
    laguerre_sum     = 0
    result           = 0
    partial_integral = 0

    for i in range(number_of_points):
        hermite_sum += hermite_function(points_hermite[i])*weight_hermite[i]

    for i in range(number_of_points):
        laguerre_sum += laguerre_function(points_laguerre[i])*weight_laguerre[i]

    if(a == "-inf"):

        if(b == "inf"):
            print("Integral: " + str(hermite_sum))
            return
        elif(b >=0):
            result = hermite_sum - laguerre_sum + numeric_integration(function, 0, b, number_of_points, False)
        else:
            result = hermite_sum - numeric_integration(function, b, 0, number_of_points, False) - laguerre_sum

    elif(b == "inf"):

        if(a == 0):
            print("Integral: " + str(laguerre_sum))
            return
        elif(a > 0):
            result = laguerre_sum - numeric_integration(function, 0, a, number_of_points, False)
        else:
            result = numeric_integration(function, a, 0, number_of_points, False) + laguerre_sum

    else:
        result = numeric_integration(function, a, b, number_of_points, polinomial_integration)
    print("Integral: " + str(result))


def numeric_integration(function, a, b, number_of_points, polinomial_integration = True):
    incognitas = []
    result     = 0

    if(polinomial_integration):
        delta_x  = float(abs(b-a)) / (number_of_points - 1)
        vector_b = []

        for i in range(1, number_of_points+1):
            incognitas.append(a+(i-1)*delta_x)
            vector_b.append(float((b**i-a**i))/i)

        vandermond_matrix = [[0.0 for i in range(number_of_points)] for j in range(number_of_points)]

        for i in range(number_of_points):
            for j in range(number_of_points):
                vandermond_matrix[i][j] = incognitas[j]**i

        matrix_a = ALC_List1.lu_decomposition(vandermond_matrix)
        x        = Matrix_Utils.backward_substitution(matrix_a, Matrix_Utils.forward_substitution(matrix_a, vector_b))

        for i in range(number_of_points):
            result += x[i]*function(incognitas[i])

    else:
        weight_legendre   = Weight_Legendre.get(number_of_points).get("weight")
        points_legendre   = Weight_Legendre.get(number_of_points).get("points")
        l                 = b-a

        for i in range(number_of_points):
            incognitas.append((a+b+points_legendre[i]*l)/2)

        integral_sum = 0

        for i in range(number_of_points):
            integral_sum += function(incognitas[i])*weight_legendre[i]

        result = integral_sum*l/2

    return result

def estimate_integral_value(function,a,b):

    m         = (b + a)/2.0
    mid_point = function(m)*(b-a)
    trapeze   = ((function(a)+function(b))/2)*(b-a)
    error     = (trapeze - mid_point)/3
    simpson   = (function(a) + (4 * function(m)) + function(b))*((b-a)/6.0)

    #mid_point_integral_value = mid_point + error
    #trapeze_integral_value   = trapeze - 2 * error
    mid_point_integral_value = mid_point
    trapeze_integral_value   = trapeze
    simpson_integral_value   = simpson

    print("Integral Mid Point: " + str(mid_point_integral_value))
    print("Integral Trapeze:   " + str(trapeze_integral_value))
    print("Integral Simpson:   " + str(simpson_integral_value))
