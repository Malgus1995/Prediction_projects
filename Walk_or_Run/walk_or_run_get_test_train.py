import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


run_label = 1
walk_lable = 0
train_address = 'train/'
test_address='test/'
run = 'run/'
walk='walk/'
train_string= "run_00061c18.png,run_5fb28fe0.png,run_a5931003.png,run_01d134fc.png,run_5fc270cc.png,run_a75e3155.png,run_021a5686.png,run_60b9d6a4.png,run_a87266f0.png,run_033697b0.png,run_61099f61.png,run_a8f6d9d2.png,run_04b620cc.png,run_61239b1c.png,run_a9232227.png,run_0648da3d.png,run_61f346be.png,run_a925bb54.png,run_07df7b55.png,run_62b8f78c.png,run_a9fdecbc.png,run_0a9284fb.png,run_62e9eaa4.png,run_ab05d1a6.png,run_0aa1d404.png,run_639f8a54.png,run_aeeb802c.png,run_0abc30f8.png,run_63f01c69.png,run_af2b304c.png,run_0b56f527.png,run_644dcb17.png,run_aff53edc.png,run_0b9180f4.png,run_6461a104.png,run_b00ca548.png,run_0c3ec7f1.png,run_68175913.png,run_b0bb739f.png,run_0c537846.png,run_6895b8bd.png,run_b10e794f.png,run_0e440581.png,run_6999e03d.png,run_b16ac748.png,run_11fe555f.png,run_69b8e96f.png,run_b19883d1.png,run_1295a1d6.png,run_6c418bb1.png,run_b540ae91.png,run_143a570e.png,run_6c7aa90f.png,run_b7d17192.png,run_144502d4.png,run_6d0a6b9f.png,run_b8c21968.png,run_14e9ec67.png,run_6f2b4633.png,run_b8c47056.png,run_15b27eec.png,run_6f6c225d.png,run_b97ca439.png,run_1685fb88.png,run_6f7aea4d.png,run_b9a4a52f.png,run_16e76f02.png,run_70982d21.png,run_b9ac5c5b.png,run_1707e727.png,run_71f336c4.png,run_b9f98417.png,run_18928876.png,run_73368ef1.png,run_ba6da104.png,run_18e7ef78.png,run_734250c1.png,run_bbea42fb.png,run_191f334f.png,run_742330c2.png,run_c0b15735.png,run_1b8d7e5a.png,run_75f8dce5.png,run_c101b372.png,run_1c7ed2a1.png,run_764d8fe3.png,run_c146dc32.png,run_1cb217e6.png,run_770667c3.png,run_c2ed65e1.png,run_1ee52c2b.png,run_772fbfd8.png,run_c3587ef1.png,run_1fed681b.png,run_7780e355.png,run_c47d3d4d.png,run_20066d30.png,run_7a3481ed.png,run_c51bd5ca.png,run_204c2085.png,run_7aa2a454.png,run_c629b320.png,run_210deb18.png,run_7b1828d4.png,run_c6aaa9c6.png,run_2473cdab.png,run_7d99207b.png,run_c6c7c567.png,run_24e1244a.png,run_7f01559d.png,run_c6e0f275.png,run_24ece0c7.png,run_7f113d88.png,run_c8410cce.png,run_255f33ed.png,run_7f825b14.png,run_c871e8c1.png,run_297cf8ba.png,run_80f77122.png,run_c88567f0.png,run_2995f395.png,run_8196e1ad.png,run_c953b99b.png,run_2b90c677.png,run_81dff100.png,run_c99641ec.png,run_2b97ed11.png,run_83b044ab.png,run_ca2b5bf0.png,run_2be0098a.png,run_83b2f9ae.png,run_ca877e3c.png,run_2d12d5b6.png,run_83bdaadc.png,run_caad1aa4.png,run_2d986c74.png,run_83e48409.png,run_cb681209.png,run_2e0e3392.png,run_84deac5c.png,run_cb79a46b.png,run_2ea5f77f.png,run_851921ec.png,run_cbe60c9d.png,run_2fe30810.png,run_862c9429.png,run_cd626cb9.png,run_3091645b.png,run_87a18e26.png,run_cd958ed9.png,run_328ff7db.png,run_8819bef9.png,run_cf693ba3.png,run_330192fb.png,run_883029d6.png,run_cf8c3366.png,run_35b521e4.png,run_883d4424.png,run_d054c079.png,run_3762a365.png,run_89376903.png,run_d15b56a6.png,run_38ea9029.png,run_8977da10.png,run_d25159e5.png,run_3955c405.png,run_8a235ba7.png,run_d2704ea9.png,run_39c1794d.png,run_8aa98f7d.png,run_d29f89b3.png,run_3a05ce65.png,run_8abfd70d.png,run_d3c49a0c.png,run_3ce0ddc5.png,run_8bdbc7bb.png,run_d5fae015.png,run_3d0b86f8.png,run_8bf6e7b3.png,run_d7749f0b.png,run_3d4f6106.png,run_8d4281d6.png,run_d7f5294f.png,run_3dedf07b.png,run_8ddd68a7.png,run_d874901d.png,run_3e5fe702.png,run_8e6e8cad.png,run_d886365d.png,run_3f199eca.png,run_8f022f03.png,run_d8bd5a21.png,run_3fec04dc.png,run_8f2595c0.png,run_db6121d5.png,run_40307acd.png,run_8f90548c.png,run_dc0dee15.png,run_40b7456d.png,run_8fd1a047.png,run_dc881a13.png,run_40c73a68.png,run_90b89869.png,run_dcee0493.png,run_41aea8d8.png,run_918ec096.png,run_e0ea1386.png,run_45c9b887.png,run_93580243.png,run_e1e80bd8.png,run_46633e2b.png,run_93829bc1.png,run_e253af3b.png,run_47cd5df2.png,run_944d070d.png,run_e429932e.png,run_48c87094.png,run_94ce1c88.png,run_e7a2eb00.png,run_494e5df1.png,run_96a67345.png,run_e959b9fe.png,run_4aa38519.png,run_975a2542.png,run_eb25643b.png,run_4b0b24dd.png,run_97ac205f.png,run_eba4867c.png,run_4b305888.png,run_984288e6.png,run_ecc49c30.png,run_4cceff3c.png,run_9a0e01be.png,run_ecd444ca.png,run_4cff1e1f.png,run_9a489899.png,run_ed5d701b.png,run_4e1b41e3.png,run_9a508437.png,run_ed8f3677.png,run_4ed46b07.png,run_9b569038.png,run_ee024937.png,run_4ed4e4fd.png,run_9bb52826.png,run_ef3ed882.png,run_4f9615de.png,run_9c1bc289.png,run_f13a6da3.png,run_52068d3d.png,run_9c43e593.png,run_f1a0e3b4.png,run_5230fa57.png,run_9d046012.png,run_f1b588f2.png,run_52730879.png,run_9d1e6d5f.png,run_f2a51a25.png,run_52d07e35.png,run_9d315f83.png,run_f335e9dd.png,run_54017fa7.png,run_9da2d846.png,run_f35a94a8.png,run_547819db.png,run_9e458faa.png,run_f3de515f.png,run_55c2b0a0.png,run_9e91c347.png,run_f470a9f7.png,run_55c45dbc.png,run_9ef7e728.png,run_f5bd3365.png,run_55d71327.png,run_a0775979.png,run_f71fab56.png,run_55fe1de2.png,run_a1d31c97.png,run_f7993f33.png,run_598fc449.png,run_a1f35e68.png,run_f8f8f0c7.png,run_59c4eb7c.png,run_a2c7f250.png,run_f9009957.png,run_59e9ef28.png,run_a379f139.png,run_fa283738.png,run_5b7ad000.png,run_a384f113.png,run_fa9389ef.png,run_5d34f556.png,run_a3f792b8.png,run_fcfacd5a.png,run_5d8b0822.png,run_a4516cad.png,run_ff531626.png,run_5efc245a.png,run_a4a252f7.png,walk_00e3d982.png,walk_5cc55431.png,walk_adf57a56.png,walk_0173e50c.png,walk_5d65ee63.png,walk_ae4f1eb9.png,walk_02852997.png,walk_5e8aecbb.png,walk_aedc6a40.png,walk_030ed8f2.png,walk_600a4487.png,walk_aef9a83e.png,walk_031ff1f1.png,walk_603e8dd7.png,walk_b0a96e8b.png,walk_03b615e2.png,walk_609a670a.png,walk_b0aba01b.png,walk_0475ca9c.png,walk_60f2892f.png,walk_b10e28ab.png,walk_048ab4b2.png,walk_627904b1.png,walk_b1501c04.png,walk_054096d9.png,walk_63ca2ca1.png,walk_b19671c7.png,walk_078a937d.png,walk_63cc78bd.png,walk_b24adc2f.png,walk_0889bc7d.png,walk_6510401f.png,walk_b3870452.png,walk_0ab43cab.png,walk_656e1a93.png,walk_b52883d8.png,walk_0bae5a2f.png,walk_658605de.png,walk_b92fefe1.png,walk_0f839625.png,walk_68055051.png,walk_b93ae0dc.png,walk_10fd9474.png,walk_68cc7990.png,walk_b9975603.png,walk_113e1597.png,walk_68e822d3.png,walk_b9d36ab6.png,walk_122d558a.png,walk_6905c3c5.png,walk_ba1fb7d6.png,walk_12e8961b.png,walk_69918fb3.png,walk_bb68114b.png,walk_12f08de0.png,walk_699d0d2d.png,walk_bbc5c41c.png,walk_157cb0b7.png,walk_69c2893c.png,walk_bcff2f38.png,walk_1616359c.png,walk_6b7a0ad9.png,walk_bdbe913a.png,walk_16acbd83.png,walk_6b9f7042.png,walk_be0c5525.png,walk_17cfba9a.png,walk_6c44ed82.png,walk_be70a3b1.png,walk_1859f826.png,walk_6d353a12.png,walk_becd3d3e.png,walk_18659c3c.png,walk_719de51d.png,walk_bfc0b7fb.png,walk_1893c656.png,walk_7254d2a3.png,walk_bfd5b9cb.png,walk_18ffe9d5.png,walk_72b9dc9c.png,walk_c09ead7a.png,walk_1ac1d89f.png,walk_74774e78.png,walk_c1861dbf.png,walk_1b7a7666.png,walk_7494b444.png,walk_c3301d4a.png,walk_1bf04186.png,walk_74a058a4.png,walk_c39ce2cd.png,walk_1ca687c9.png,walk_74feca8e.png,walk_c465af86.png,walk_1caabdd0.png,walk_7579d335.png,walk_c4eec76f.png,walk_1d81a125.png,walk_76210243.png,walk_c9020c81.png,walk_1e8c7768.png,walk_7624aed7.png,walk_c9f7ff26.png,walk_1ee72c37.png,walk_77ab8966.png,walk_ca413bb5.png,walk_1eee9821.png,walk_78991116.png,walk_ca73bd6b.png,walk_20015ab9.png,walk_791ae960.png,walk_cb0f02db.png,walk_236a0ed2.png,walk_7999e5b2.png,walk_cc36a8a4.png,walk_237eafc4.png,walk_7a6be96a.png,walk_cc7ffa64.png,walk_2383d608.png,walk_7b0458fd.png,walk_ce047069.png,walk_23d11643.png,walk_7b1394c7.png,walk_cf049467.png,walk_2425f711.png,walk_7b238d44.png,walk_cf1be335.png,walk_246c28c0.png,walk_7b344bdd.png,walk_cf47b62f.png,walk_24f3368c.png,walk_7c7c0fbb.png,walk_cf5d71e2.png,walk_2750f643.png,walk_7ce332ae.png,walk_cf63d904.png,walk_27d8ccfa.png,walk_7d2756ee.png,walk_cff648b7.png,walk_2850aef7.png,walk_7ed35c7e.png,walk_d1bdb351.png,walk_2894196b.png,walk_7f2bb059.png,walk_d25d5fc4.png,walk_2994b653.png,walk_8000cf22.png,walk_d2e63fe9.png,walk_2a7614cd.png,walk_80279bc5.png,walk_d37870c7.png,walk_2be55839.png,walk_82c3b0f9.png,walk_d44fe5fd.png,walk_2f2418ab.png,walk_82cdb83e.png,walk_d66372ee.png,walk_30dc570f.png,walk_82eec80c.png,walk_d77872d1.png,walk_3140b0d5.png,walk_8404e089.png,walk_d82f0ba5.png,walk_31e77b40.png,walk_84550a2e.png,walk_d83bc1a0.png,walk_32fa46b8.png,walk_8489e345.png,walk_d842dbed.png,walk_3398e2a7.png,walk_84aaae81.png,walk_d8960d01.png,walk_346fe00e.png,walk_86c260a4.png,walk_d9848c10.png,walk_3579891f.png,walk_87187f17.png,walk_dbffae47.png,walk_358e1873.png,walk_879d83fd.png,walk_dcbf1448.png,walk_361bc465.png,walk_897205e8.png,walk_dcc14183.png,walk_365dba1a.png,walk_8c005c50.png,walk_dd5631a7.png,walk_370001cd.png,walk_8c6d5789.png,walk_de665266.png,walk_3737e542.png,walk_8d129c64.png,walk_deffae11.png,walk_373f719c.png,walk_8e7c69fd.png,walk_e0971b24.png,walk_37b400d6.png,walk_8f232bfe.png,walk_e0e29611.png,walk_39237fdd.png,walk_8f76e0c5.png,walk_e1675d0a.png,walk_3e3a33d8.png,walk_8f9d2347.png,walk_e20f666b.png,walk_3e4348dc.png,walk_8fe30c6e.png,walk_e2e4ae34.png,walk_3ee5b835.png,walk_9026d006.png,walk_e3ba54dd.png,walk_3f4723b7.png,walk_9095121e.png,walk_e3dd0f06.png,walk_3fa35227.png,walk_913c92fb.png,walk_e4fe74e3.png,walk_40446d44.png,walk_92d877cf.png,walk_e6eb935f.png,walk_405ec40e.png,walk_93032ff5.png,walk_e8440bbe.png,walk_40bbc0c2.png,walk_9401b98d.png,walk_e913d3f9.png,walk_41eada3e.png,walk_95ecf6de.png,walk_ea26a17f.png,walk_42482c7b.png,walk_991d1b3f.png,walk_eb55a092.png,walk_42574283.png,walk_9974f8ad.png,walk_ec153caa.png,walk_438ba398.png,walk_9abf671a.png,walk_ee4e5f4f.png,walk_4436d1e7.png,walk_9d27ec88.png,walk_eea7516b.png,walk_451f5d5a.png,walk_9de03315.png,walk_f00ca35d.png,walk_474b6f9d.png,walk_9f099ade.png,walk_f05c9540.png,walk_47b25bd2.png,walk_9ffd8fb1.png,walk_f0f1fc6a.png,walk_48fc53bb.png,walk_a0f26e42.png,walk_f18a1a50.png,walk_49ac6f6e.png,walk_a1083271.png,walk_f1cb7d25.png,walk_4b9cf2c0.png,walk_a1b1aea5.png,walk_f200c493.png,walk_4e0263b4.png,walk_a21fd782.png,walk_f20f0703.png,walk_4e55afdc.png,walk_a2709922.png,walk_f34b22f0.png,walk_4ecc979c.png,walk_a285f87e.png,walk_f411a00d.png,walk_4f0c3d24.png,walk_a2f51f74.png,walk_f59ba6f2.png,walk_4fa38ec0.png,walk_a39076be.png,walk_f5b1f023.png,walk_4fa48861.png,walk_a4a95c7b.png,walk_f640b242.png,walk_4fef4038.png,walk_a4b5e93c.png,walk_f6963aa6.png,walk_51a414fc.png,walk_a6023e8c.png,walk_f6fe3b3a.png,walk_52e727ef.png,walk_a66b1744.png,walk_f7cb66cc.png,walk_5389e1f2.png,walk_a66c0848.png,walk_f827add5.png,walk_54fbf051.png,walk_a81a8fe0.png,walk_fcf3fa51.png,walk_55d8b174.png,walk_a8710352.png,walk_fe3afb34.png,walk_5af02106.png,walk_a88e671b.png,walk_ff912309.png,walk_5b27f6db.png,walk_aaac4c96.png,walk_5b32f2d3.png,walk_ab3edbdf.png"
address_index=0
train_arr = []
for string in train_string.split(","):
    train_arr.append(train_address+(run if address_index<299 else walk)+string)
    address_index+=1
def one_hot(labels):
    label_ = np.array([[0,0]]*len(labels))
    for i in range(len(label_)):
        j= labels[i]
        label_[i][j]=1
    return label_
    
def shuffle_data(train_x,labels_Y):
    train_indices = list(range(len(train_x)))
    np.random.shuffle(train_indices)
    shuffled_x = [train_x[idx] for idx in train_indices]
    labels = [labels_Y[idx] for idx in train_indices]
    return shuffled_x,labels
    
def _parse_function(filename):
  image_string = tf.read_file(filename)
  image_decoded = tf.image.decode_png(image_string)
  return image_decoded

train_img = []
train_labels =[run_label]*299+[walk_lable]*301

for train_piece in train_arr:
   run = _parse_function(train_piece)
   train_img.append(run)


indices = np.random.choice(range(1,600),500)
batch_img = [train_img[idx] for idx in indices]
batch_label = [train_labels[idx] for idx in indices]

test_img = []
test_label = []


test_string="run_0794de59.png,run_639a2946.png,run_b16636b7.png,run_0987572f.png,run_6b986002.png,run_b56d5e91.png,run_0b30ced7.png,run_6c717b45.png,run_b5ff0667.png,run_0c98676d.png,run_6dd1dbbd.png,run_bbbc236a.png,run_1073489f.png,run_7148ac65.png,run_bde9d918.png,run_13662896.png,run_7244bb3e.png,run_be2d5f70.png,run_1bb05084.png,run_7666656e.png,run_c4e7d0ef.png,run_1ff02911.png,run_78b39d88.png,run_c9f91d3a.png,run_20dcdbec.png,run_7b173abd.png,run_d7979a13.png,run_26e292d1.png,run_7cd0ad06.png,run_dc393379.png,run_274eaee3.png,run_7d5af605.png,run_dc953638.png,run_2aab0e1b.png,run_8064cca3.png,run_dcd4f931.png,run_2b758aeb.png,run_82ee1773.png,run_df48f40f.png,run_2bae0a9d.png,run_838fadaa.png,run_df6c7bfc.png,run_2fe546c8.png,run_849d4f97.png,run_e03c8978.png,run_3252a749.png,run_8713cf1c.png,run_e15921b4.png,run_34713f03.png,run_8ceeeca7.png,run_ef7f2500.png,run_365fa2e5.png,run_90d5412b.png,run_f02b25c8.png,run_3aa2c4e5.png,run_9417fa3e.png,run_f2e85951.png,run_3b89e223.png,run_94545263.png,run_f3750b68.png,run_3d46b336.png,run_94f53a29.png,run_f4bc7985.png,run_3d560204.png,run_9ac4b498.png,run_f54c4d53.png,run_3ea8d56c.png,run_9b0e163e.png,run_f84978c2.png,run_412b17b7.png,run_9baf8e76.png,run_fd35e643.png,run_41b7236f.png,run_9d419641.png,run_fe77938f.png,run_434d009d.png,run_a0564e69.png,run_fee36129.png,run_47e8074d.png,run_acc06cbc.png,run_603ac08a.png,run_b0f5ef5d.png,walk_035124b5.png,walk_55fc48a4.png,walk_b7ae679c.png,walk_0c96b662.png,walk_5924fa61.png,walk_b9db848a.png,walk_1078e68d.png,walk_5bd87f4e.png,walk_c95d8645.png,walk_125cac5b.png,walk_5cb390fe.png,walk_cdd1ca66.png,walk_158c0f76.png,walk_5f25a007.png,walk_d06fab89.png,walk_1aa6836f.png,walk_5ff2a9a1.png,walk_d20904e9.png,walk_1eb5234a.png,walk_6c57b9b3.png,walk_d3af9d4c.png,walk_20564b8d.png,walk_73df008e.png,walk_e46826c9.png,walk_21c38b60.png,walk_79cb786b.png,walk_e47417b0.png,walk_2d18506d.png,walk_801f1410.png,walk_e5fb5c62.png,walk_3af52937.png,walk_8304a88c.png,walk_e9ac206a.png,walk_3ba0de08.png,walk_96584b43.png,walk_ee0ee9a8.png,walk_3f87901d.png,walk_98cfe2a0.png,walk_f3db2268.png,walk_3fb09ff7.png,walk_99774583.png,walk_f41d20a0.png,walk_4312afdd.png,walk_9b6b8438.png,walk_f5d58cea.png,walk_4416ab19.png,walk_9c35d4b1.png,walk_f8b5d2db.png,walk_443d602c.png,walk_9d193f21.png,walk_f96e47a5.png,walk_46844120.png,walk_9e646bbc.png,walk_fc359360.png,walk_4d412d2a.png,walk_ac2e711d.png,walk_fe9e5656.png,walk_54e056b6.png,walk_b37fa854.png"
test_run_len = 82
test_walk_len= len(test_string.split(',')) - test_run_len
run = 'run/'
walk='walk/'
test_list=test_string.split(',')
address_index=0
for string in test_list:
    test_img.append(test_address+(run if address_index<82 else walk)+string)
    address_index+=1
      
    
test_label = test_run_len*[run_label]+test_walk_len*[walk_lable]
test_indices = range(141)
test_indices =np.random.choice(test_indices,10)
test_img = [test_img[i] for i in test_indices]
train_labels = one_hot(train_labels)
train_img,train_labels = shuffle_data(train_img,train_labels)
test_label = one_hot(test_label)
test_label = [test_label[i] for i in test_indices]
test_img =[_parse_function(test_img[i]) for i in range(len(test_img))]
