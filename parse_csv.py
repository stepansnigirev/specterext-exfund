from embeed.specterext.massfund.util import *

DATA = """
Serial Number,Address,Amount
EB000001,bc1q0k4k25pxhhaumewtylxh4wlxrn5krclgh66hgh,100
EB000002,bc1qf0lrc7reacxyrla64elepf6um93prksznc76ks
EB000003, bc1q0f90ha2pv4yeg8e5mhrjc387ga0h9njjpxg8z4,
EB000004,bc1qwe90yqy27n77a63arpnwgrsgypxydh4dearhnv
EB000005,bc1qsh874fsrvedpplyk0yq6ehn95rmwg6xll6mgq6
EB000006,bc1qxax5vwymva3jvu7czzkk8r35s7hfwpxndauwum
EB000007,bc1qy54pzdept56m4540sc8sqel0h45wkdd8ta4d43
EB000008,bc1qe9qgehhhtjs4pksclpjexqr70u4m28nrcwa20j
EB000009,bc1q39h532g2glgafthz0pyrh706d4ztpm9c9cs685
EB000010,bc1qfjanrfa2dex9hu7x0xe6lma9pdk8jdnmteclwe
EB000011,bc1q3aluth99pk396z8u4ngk525lx43f7mxfu8pyfl
EB000012,bc1q773y6c4kup73cxggl6604ysq4afekuk0kmdksv
EB000013,bc1q8twzjfcawp7xd4qlvf2khg2hevzay6kc00nqnz
EB000014,bc1qhu44kl004te5w048xvgqp9x4mkguef6yeweq7j
EB000015,bc1qgs26a44p0zuy4uxqcteaws2n4emturt87kq9d8
EB000016,bc1qul96x5jpkuauu89y9adldnw9klh0gr5pgllqav
EB000017,bc1qlmchdck6ttjk57p6f8vercll98smfm93f5rjhn
EB000018,bc1q8tzh52u527d3hwv4lgmpa2xw50sr3d8mnldxm8
EB000019,bc1qswplwpff44fpypddhh5wv8lc2xmeamvs7h6ry8
EB000020,bc1qqp277h7urrm53avt656uhx9ngl8c9lxc6u8mz0
EB000021,bc1q2mle6duvnwamjx5pgwm94dqprwkkdh0p5dlut6
EB000022,bc1qnq9alxnc243uy32l3r828cwahhvu4mr8kadph6
EB000023,bc1qamcdaalsdagvhz930mzsmfyvdexcgzyze0jumz
EB000024,bc1qjwkyc9sx3f8ahmzmkftsl5ewyz42rsvsjgzhlf
EB000025,bc1q60aehcjzh5stjzt83ta72fymgz802999a560ak
"""

DATA = """
Serial number,Address
m/84'/1'/0'/0/0,bcrt1qe2lmnwnmu7avpr2htnvwsu0z8886dkh0gj0hms,,
m/84'/1'/0'/0/1,bcrt1qr7d9ektwguscl6mtgt406kesrjdxxtnt9xkvrn,,
m/84'/1'/0'/0/2,bcrt1qr54ct3lmuytux2ut9vvmphxgsrwrduggnahqqe,,
m/84'/1'/0'/0/3,bcrt1qnk6p4ker2zkxeez9dymjd3g6j6xctceqlnsk6e,,
m/84'/1'/0'/0/4,bcrt1qgp9dpv2fjszfe70d9c4jweadedrzlgc38lpyym,,
m/84'/1'/0'/0/5,bcrt1qfqg6jxr7ykw8329t6ehfw7qsqe5u4nuavetmpm,,
m/84'/1'/0'/0/6,bcrt1qgfcg8df8u39np8xz8msu4p7vvewv42vlxdap56,,
m/84'/1'/0'/0/7,bcrt1qggjznaymue53nzygy956q43gmwyvamdgtmfa5x,,
m/84'/1'/0'/0/8,bcrt1q0tujnmff0qvv4lxtywr804q56jp4sjkfklea7n,,
m/84'/1'/0'/0/9,bcrt1qshjxwysyrhgcxkqh3a09h5rzxx3nn32mxr34he,,
m/84'/1'/0'/0/10,bcrt1q3vwpyg09uafwmzakg679lxcck9ej5jppzacy49,,
m/84'/1'/0'/0/11,bcrt1q8262397ysd4uawa76zctru4xe42xka8hn0xlma,,
m/84'/1'/0'/0/12,bcrt1qrsl9xrk92wtcnp68w3dels0hp7kqntjs6t44md,,
m/84'/1'/0'/0/13,bcrt1qqyz8sv9mu7nhl2uq9q3wuuwseydntvrrz7kfu6,,
m/84'/1'/0'/0/14,bcrt1qwg2vf27knm5lxjsv6ygvk4a9n7keepzyznertt,,
m/84'/1'/0'/0/15,bcrt1qd6g5xg0w0w30jjc7tq2fnkge9q95l4ca2vw0ed,,
m/84'/1'/0'/0/16,bcrt1qyy04s2cjufa9494ywt64zmrv6crnzqr0at4vlt,,
m/84'/1'/0'/0/17,bcrt1q2d6j9pqchm2ds8y792s9mhjcsakqp49ajzahn9,,
m/84'/1'/0'/0/18,bcrt1qsu28up6uf3nst5hd8w4gnef0q7spetqusnkwyv,,
m/84'/1'/0'/0/19,bcrt1qptm8uqqw8wr6l0che5a3lztsrna3zsz9v503f9,,
"""

def main():
    print(parse_csv(DATA))

if __name__ == '__main__':
    main()