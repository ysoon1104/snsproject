import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False

# =====================================
# 📊 샘플 데이터 (SNS 사용시간별 영향)
# =====================================
sns_hours = ['1시간 이하', '1~2시간', '2~3시간', '3~4시간', '4시간 이상']
study_score = [78, 75, 73, 71, 68]        # 학업 성취도
sleep_quality = [82, 79, 76, 74, 70]      # 수면 질
stress_level = [30, 35, 42, 50, 62]       # 스트레스 지수
concentration = [80, 77, 74, 70, 65]      # 집중력

x = np.arange(len(sns_hours))

# =====================================
# 🎨 그래프 1: Y축 조정 꺾은선 그래프
# =====================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('📱 SNS 사용시간이 학생에게 미치는 영향', 
             fontsize=16, fontweight='bold', y=1.02)

# --- 그래프 1-1: 학업 성취도 (Y축 조정) ---
ax1 = axes[0, 0]
ax1.plot(sns_hours, study_score, 
         color='#E74C3C', marker='o', linewidth=2.5, 
         markersize=8, markerfacecolor='white', markeredgewidth=2)
ax1.fill_between(sns_hours, study_score, alpha=0.1, color='#E74C3C')

# Y축 범위 조정 (핵심!)
ax1.set_ylim(60, 85)

# 데이터 레이블 표시
for i, v in enumerate(study_score):
    ax1.annotate(f'{v}점', (sns_hours[i], v), 
                textcoords="offset points", 
                xytext=(0, 10), ha='center', fontsize=9,
                color='#E74C3C', fontweight='bold')

ax1.set_title('📚 학업 성취도', fontweight='bold', pad=10)
ax1.set_ylabel('점수')
ax1.set_xlabel('SNS 사용시간')
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.tick_params(axis='x', rotation=15)

# --- 그래프 1-2: 수면 질 (Y축 조정) ---
ax2 = axes[0, 1]
ax2.plot(sns_hours, sleep_quality, 
         color='#3498DB', marker='s', linewidth=2.5,
         markersize=8, markerfacecolor='white', markeredgewidth=2)
ax2.fill_between(sns_hours, sleep_quality, alpha=0.1, color='#3498DB')

ax2.set_ylim(60, 90)

for i, v in enumerate(sleep_quality):
    ax2.annotate(f'{v}점', (sns_hours[i], v),
                textcoords="offset points",
                xytext=(0, 10), ha='center', fontsize=9,
                color='#3498DB', fontweight='bold')

ax2.set_title('😴 수면 질', fontweight='bold', pad=10)
ax2.set_ylabel('점수')
ax2.set_xlabel('SNS 사용시간')
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.tick_params(axis='x', rotation=15)

# --- 그래프 1-3: 스트레스 지수 (막대 그래프) ---
ax3 = axes[1, 0]
colors = ['#2ECC71', '#F1C40F', '#E67E22', '#E74C3C', '#8E44AD']
bars = ax3.bar(sns_hours, stress_level, color=colors, 
               edgecolor='white', linewidth=1.5, width=0.6)

ax3.set_ylim(20, 70)

for bar, v in zip(bars, stress_level):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{v}점', ha='center', va='bottom', 
             fontsize=9, fontweight='bold')

ax3.set_title('😰 스트레스 지수', fontweight='bold', pad=10)
ax3.set_ylabel('지수')
ax3.set_xlabel('SNS 사용시간')
ax3.grid(True, alpha=0.3, linestyle='--', axis='y')
ax3.tick_params(axis='x', rotation=15)

# --- 그래프 1-4: 집중력 (수평 막대 그래프) ---
ax4 = axes[1, 1]
colors2 = ['#1ABC9C', '#27AE60', '#F39C12', '#E74C3C', '#C0392B']
bars2 = ax4.barh(sns_hours, concentration, color=colors2,
                 edgecolor='white', linewidth=1.5, height=0.6)

ax4.set_xlim(55, 88)

for bar, v in zip(bars2, concentration):
    ax4.text(v + 0.3, bar.get_y() + bar.get_height()/2,
             f'{v}점', ha='left', va='center',
             fontsize=9, fontweight='bold')

ax4.set_title('🧠 집중력', fontweight='bold', pad=10)
ax4.set_xlabel('점수')
ax4.set_ylabel('SNS 사용시간')
ax4.grid(True, alpha=0.3, linestyle='--', axis='x')

plt.tight_layout()
plt.savefig('sns_영향_기본그래프.png', dpi=150, bbox_inches='tight')
plt.show()


# =====================================
# 🎨 그래프 2: 기준값 대비 변화량 그래프
# =====================================
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 5))
fig2.suptitle('📉 1시간 이하 대비 변화량 비교', 
              fontsize=14, fontweight='bold')

# 기준값(1시간 이하) 대비 변화량 계산
study_change = [v - study_score[0] for v in study_score]
stress_change = [v - stress_level[0] for v in stress_level]
sleep_change = [v - sleep_quality[0] for v in sleep_quality]
conc_change = [v - concentration[0] for v in concentration]

# --- 변화량 막대 그래프 (학업/수면/집중력) ---
ax5 = axes2[0]
width = 0.25
x = np.arange(len(sns_hours))

bars_study = ax5.bar(x - width, study_change, width, 
                     label='학업 성취도', color='#E74C3C', alpha=0.8)
bars_sleep = ax5.bar(x, sleep_change, width,
                     label='수면 질', color='#3498DB', alpha=0.8)
bars_conc = ax5.bar(x + width, conc_change, width,
                    label='집중력', color='#2ECC71', alpha=0.8)

ax5.axhline(y=0, color='black', linewidth=1.5, linestyle='-')
ax5.set_title('📚 부정적 지표 변화량', fontweight='bold')
ax5.set_ylabel('변화량 (점)')
ax5.set_xlabel('SNS 사용시간')
ax5.set_xticks(x)
ax5.set_xticklabels(sns_hours, rotation=15)
ax5.legend()
ax5.grid(True, alpha=0.3, linestyle='--', axis='y')

# 레이블
for bar in bars_study:
    h = bar.get_height()
    ax5.text(bar.get_x() + bar.get_width()/2, 
             h - 0.5 if h < 0 else h + 0.1,
             f'{h:+.0f}', ha='center', va='top' if h < 0 else 'bottom',
             fontsize=7, color='#E74C3C')

# --- 변화량 꺾은선 (스트레스) ---
ax6 = axes2[1]
ax6.plot(sns_hours, stress_change, 
         color='#8E44AD', marker='^', linewidth=2.5,
         markersize=10, label='스트레스 증가량')
ax6.fill_between(sns_hours, stress_change, 0, 
                 alpha=0.2, color='#8E44AD')
ax6.axhline(y=0, color='black', linewidth=1.5)

for i, v in enumerate(stress_change):
    ax6.annotate(f'{v:+d}점', (sns_hours[i], v),
                textcoords="offset points",
                xytext=(0, 12), ha='center', fontsize=9,
                color='#8E44AD', fontweight='bold')

ax6.set_title('😰 스트레스 변화량', fontweight='bold')
ax6.set_ylabel('변화량 (점)')
ax6.set_xlabel('SNS 사용시간')
ax6.grid(True, alpha=0.3, linestyle='--')
ax6.tick_params(axis='x', rotation=15)

plt.tight_layout()
plt.savefig('sns_영향_변화량그래프.png', dpi=150, bbox_inches='tight')
plt.show()


# =====================================
# 🎨 그래프 3: 레이더 차트 (종합 비교)
# =====================================
fig3, axes3 = plt.subplots(1, 3, figsize=(15, 5),
                            subplot_kw=dict(polar=True))
fig3.suptitle('🕸️ SNS 사용시간별 종합 영향 레이더 차트',
              fontsize=14, fontweight='bold')

categories = ['학업성취도', '수면 질', '집중력', '정서안정\n(스트레스역)', '생활만족도']
N = len(categories)

# 생활만족도 임의 데이터
life_satisfaction = [85, 80, 74, 68, 60]
# 스트레스 역수 변환 (높을수록 좋게)
stress_inv = [100 - v for v in stress_level]

# 각 그룹별 데이터
all_data = [
    [study_score[i], sleep_quality[i], concentration[i], 
     stress_inv[i], life_satisfaction[i]] 
    for i in range(5)
]

# 대표 3구간만 표시
show_idx = [0, 2, 4]
show_labels = ['1시간 이하', '2~3시간', '4시간 이상']
show_colors = ['#2ECC71', '#F39C12', '#E74C3C']

angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

for idx, (data_idx, label, color, ax) in enumerate(
        zip(show_idx, show_labels, show_colors, axes3)):
    
    values = all_data[data_idx]
    values += values[:1]
    
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.plot(angles, values, 'o-', linewidth=2, color=color)
    ax.fill(angles, values, alpha=0.25, color=color)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=8)
    ax.set_ylim(0, 100)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(['20', '40', '60', '80', '100'], size=6)
    ax.set_title(f'📱 {label}', fontweight='bold', pad=15, color=color)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sns_영향_레이더차트.png', dpi=150, bbox_inches='tight')
plt.show()

print("✅ 그래프 3종 생성 완료!")
print("📁 저장된 파일:")
print("   - sns_영향_기본그래프.png")
print("   - sns_영향_변화량그래프.png")
print("   - sns_영향_레이더차트.png")
