from itertools import combinations
inp = """44
17
23
42
25
26
6
45
30
8
15
39
28
16
20
50
14
47
27
7
13
46
34
24
32
19
21
31
22
23
33
41
92
29
30
70
45
26
35
28
48
50
20
36
27
37
53
42
49
39
44
43
61
51
68
46
73
138
47
56
69
63
55
57
96
64
59
79
66
108
76
106
95
88
82
119
97
192
93
103
137
135
102
104
111
112
150
123
116
125
130
249
268
142
356
191
196
181
227
288
303
190
329
213
205
206
215
498
216
313
228
239
241
255
272
311
347
441
323
371
377
403
386
396
420
395
480
488
418
411
617
455
444
467
483
469
494
636
527
694
634
724
700
947
1641
763
781
782
898
806
1035
829
855
2422
880
899
911
1021
1547
963
996
1130
1221
1630
1328
1334
1424
1463
1544
1545
1563
1587
2399
1704
1635
2304
4126
1735
1779
1932
1810
1959
5671
2093
3723
3150
2351
2878
2662
3990
2758
2887
3279
3323
3108
3198
5507
3370
3663
5986
9633
3514
6083
3589
3742
3769
4052
4444
4851
5013
5109
6401
6649
5420
5645
11662
6967
6477
8755
6306
10135
6884
7566
7103
7256
7283
8527
7331
11411
12010
9864
10271
9295
12365
10122
17418
11065
13580
18765
11951
12783
24793
21246
32124
13190
26021
16861
16551
14359
15783
15810
16626
17195
27194
25973
19159
19417
20360
25141
21187
30131
30441
24734
26310
27142
41988
32334
29741
35227
27549
31554
32978
30142
49586
31593
34969
33821
43168
38576
39519
40604
39777
49875
45921
47497
72231
51044
51876
53452
54691
57290
57691
59103
66799
89660
61696
67947
61735
65414
66562
68790
72397
78095
80381
87016
85698
97372
97797
93418
98541
110979
108735
120666
108143
133361
114981
116794
164359
123431
127110
226779
146885
127149
131976
135352
141187
150492
224937
297720
197995
179116
195169
201561
214084
206684
231775
216878
228809
258635
243943
456630
240225
262462
282468
254259
385800
259125
352086
267328
276539
393200
329608
374285
377111
380677
588733
453804
486034
423562
435493
652371
445687
609486
484168
494484
779000
981979
513384
521587
644439
526453
535664
628625
713015
606147
1150212
1322501
1508432
869249
804239
1226399
859055
881180
907730
948877
1138923
1224687
1503494
978652
1057251
1142009
1239468
1407633
1048040
1484541
1164289
1432864
1792914
2556472
2464510
1750429
1753116
1673488
1685419
1830057
1740235
1766785
1788910
1996917
1927529
2026692
3074732
2911127
2212329
3236385
2190049
2840954
2597153
2480904
2957203
3118283
3106352
4337388
3358907
3413723
3440273
3618967
3425654
3452204
3924446
5103269
3978959
3716439
5642253
4787202
4216741
5264781
6429070
5833538
4670953
5031003
9358692
10620740
6465259
6063555
6224635
8766161
13553363
7032690
6853996
9858994
6877858
7350100
17005567
7640885
7695398
7933180
11649619
10429455
10295784
19979432
9701956
10504491
10734508
12063693
11255638
12288190
13731854
12528814
30558930
41293438
18917689
13886686
13910548
14204096
14227958
14518743
21945403
15336283
17342841
18951036
17635136
19997740
20131411
20206447
20436464
22792681
32494637
21990146
23319331
23784452
26492286
33469779
35900694
28090782
28432054
27797234
28114644
28138506
28722839
28746701
29855026
57652260
26134589
46065680
37841583
37632876
40204187
40337858
52931101
45309477
44782827
45774598
47103783
49453920
49919041
52626875
53931823
54225371
54273095
69060697
54249233
56837483
74032316
54857428
83616181
70917416
63767465
83151060
83407474
75474459
77837063
95195286
104192136
107180334
90092304
187599610
99706421
103941266
99372961
102545916
106558698
108157194
294779944
128305411
180591014
109106661
120604948
186162097
118624893
139241924
134684881
208479622
319832938
161244537
229711609
173032349
185287590
227678372
196651002
189465265
315275895
199079382
201918877
228762142
288748208
316636816
217263855
239229841
243791542
227731554
248348585
259846872
320543770
455409926
397944887
400998259
703758511
334276886
346532127
425413144
388544647
441148718
386116267
391384142
523742151
416343237
438309223
446025997
1149784508
466961395
444995409
456493696
635175684
548275324
476080139
508195457
580390642
775425604
813957791
680809013
1021539360
1566127745
720393153
735076774
774660914
779928789
777500409
836379551
1259983788
883304632
1588618705
1554589703
891021406
943041534
901489105
964689153
984275596
1440769292
1253580548
1228588610
1088586099
1261199655
1494766804
1517188564
1681417894
1455469927
1495054067
1497893562
1927317130
1552161323
1742189562
2458918303
2204241189
1774326038
1784793737
2817207315
1792510511
1834062940
1844530639
3534700073
2684058537
2726482172
3457821737
2317174709
3269092842
3423607456
2716669582
3608388978
3259378126
2950523994
2953363489
6992521810
3815068271
3294350885
3577304248
10261614652
5421834887
4048771828
5442451918
3618856677
5882834768
3626573451
4797894128
5586267551
5774996446
5267698703
5033844291
5270538198
7863840099
5667193576
5670033071
8529916324
5903887483
6579936940
9288889748
8375198376
6871655133
7196160925
6913207562
7203877699
7245430128
7667628505
7675345279
11256300622
8416750805
8897111649
14539283638
9831738419
10304382489
10301542994
22914482014
10701037867
18452461547
11337226647
13334822081
15401571457
16791949181
22623711829
13451592073
14067816058
19198654643
13784862695
14871506204
14117085261
19004855152
14920775407
21460207974
16092096084
25240321505
23753135067
24703244623
20532776286
24768853925
21641609136
21002580861
22038264514
24035859948
35874087065
28988591465
27119684776
27236454768
27519408131
27568677334
27852678753
44568636234
28656368899
59909947013
29037860668
30209181345
33925630559
31012871491
40795340707
36624872370
61045315335
55089133521
41535357147
51850790481
43679873650
42644189997
50040441529
46074124462
51155544724
54688362110
56507999596
54639092907
54755862899
55088085465
55421356087
56509047652
64134811904
57694229567
59247042013
61222052836
66834053715
64938502050
105129575050
115861145743
78160229517
84179547144
85215230797
88718314459
86324063647
105461797616
100338419564
96114565991
100713217369
105794637631
111930403739
109394955806
113115585654
109843948364
110509441552
206175014985
114203277219
171066001200
116941271580
120469094849
128056106551
183775325295
151262565697
180294113135
222510541460
200648718198
173933545256
171539294444
175042378106
220807514413
196452985555
196827783360
201909203622
206507855000
215189593437
221325359545
230056857234
300763207984
220353389916
244997378131
231144548799
265465842916
237410366429
248525201400
375691096304
364069438430
325196110953
485935567829
345472839700
346581672550
348975923362
482407744560
371870161466
539111816536
403335638360
620395362866
398736986982
423234563167
451497938715
496610391715
478582058634
450410247150
468554915228
457763756345
648333016491
687820613579
723345934258
562606477382
573721312353
670668950653
671777783503
674172034315
692054512250
694448763062
770607148448
1036796536941
775205799826
795104724633
1007666731764
1446983583329
1183001840248
919844954882
928992305784
901908185865
947136973862
2111994146032
1024131559503
1576080220180
1340387528741
1136327789735
1415400446508
1345949817818
1233275428035
1244390263006
1386503275312
1363832295753
1681838766079
1462661660698
1465055911510
1545812948274
2315495581096
1570310524459
1697012910498
1821753140747
2102846795130
1830900491649
3730896027604
1849045159727
1926039745368
2706638314194
2160459349238
2257406987538
2369603217770
2380718052741
2477665691041
2579225245853
2590340080824
2779088376309
4044281157363
2750335571065
4106452147265
2927717572208
3008474608972
3546058070225
3803219935812
3924599935877
3267323434957
4505264991221
3652653632396
3679945651376
3756940237017
4555683473921
6631238250071
5915661287995
4417866336776
4530062567008
4627010205308
5378077826742
4858383743782
5056890936894
5169565326677
5529423947374
9840261223872
5758810180037
6195041007165
7332599283772
10822051212473
6275798043929
6947269086333
7409593869413
7191923370834
10459246805791
10586314884268
7436885888393
8097811988152
8973549810697
14524522654606
8947928903784
9044876542084
9276250080558
9157072772316
9485393949090
11805652830115
9915274680676
10226456263571
10928375506714
16410435699090
11953851187202
12034608223966
14139192457167
13223067130262
15432870816245
13467721414763
18981877310299
14601517240247
14628809259227
15534697876545
16384814792177
16481762430477
18130622583013
17921478714481
22512597956847
17992805445868
27467479040211
18433322852874
19383529035887
19400668629766
22962983730680
22882226693916
21154831770285
23988459411168
25176918317464
27362259587429
25257675354228
27824584370509
29002419291308
35980319371610
28069238655010
29230326499474
35756349010532
35914284160349
35865291466364
34474567876345
34403241144958
41913266586613
61870720185169
37833991482640
48613855535361
37816851888761
58988823252925
63825587665542
40555500400051
50157251061593
44037058464201
46412507124513
52057698066178
50434593671692
52619934941657
53082259724737
55893823025519
72237232627598
57299565154484
63633567644432
76420791866415
71621640476896
68877809021303
70268532611322
72220093033719
79730118475374
75650843371401
84246498607153
78372352288812
81853910352962
90712751461644
84592558864252
121497743962960
86968007524564
90449565588714
94471652135893
96847100796205
102492291737870
103054528613349"""
inp  = [int(k) for k in inp.split("\n")]
# part 1
# for index in range(25, len(inp)):
#     number = inp[index]
#     reached = False
#     for otherone, othertwo in combinations(inp[index-25:index],2):
#         if otherone + othertwo == number:
#             reached = True
#             break
#     if not reached:
#         print(number)
#         exit(0) # output: 26134589
# part 2
left, right = 0, 1
runningsum = inp[left] + inp[right]
while right < len(inp):
    if runningsum < 26134589:
        right += 1
        runningsum += inp[right]
        continue
    elif runningsum > 26134589:
        if left < right - 1:
            left += 1
            runningsum -= inp[left-1]
            continue
        else:
            right += 1
            runningsum += inp[right]
    else:
        print(left) # output: 387
        print(inp[left])
        print(right) # output: 403
        print(inp[right])
        print(runningsum)
        print(inp[left:right+1])
        print("weakness: ")
        print(max(inp[left:right]) + min(inp[left:right])) # output: 3535124
        exit(0)