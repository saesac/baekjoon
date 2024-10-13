for _ in range(int(input())):
    h, m, s = map(int, input().split())
    h_angle = h*30 + m/2 + s*360/12/60/60
    m_angle = m*6 + s/10
    s_angle = s*6
    HM = min(abs(h_angle - m_angle), 360 - abs(h_angle - m_angle))
    MS = min(abs(m_angle - s_angle), 360 - abs(m_angle - s_angle))
    SH = min(abs(s_angle - h_angle), 360 - abs(s_angle - h_angle))
    print(min(HM, MS, SH))