import numpy as np
import xlwings as xw
import matplotlib.pyplot as plt
from matplotlib import gridspec
from pprint import pprint
import datetime

def draw_serveity_bar(mildMeans,moderateMeans,severeMeans,fatalMeans,state_list):
    """
    :param mildMeans 轻微BUG统计list
    :param moderateMeans 一般BUG统计list
    :param severeMeans 严重BUG统计list
    :param fatalMeans 致命BUG统计list
    """
    # https://blog.csdn.net/huanyingzhizai/article/details/90479836
    table_vals=[]
    fontsize = 14
    gs = gridspec.GridSpec(16,1) #表格和柱形图的分布
    N = len(state_list)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence

    grid01 = plt.subplot(gs[:12,0])
    p1 = grid01.bar(ind, mildMeans, width,color='#FFFF00')
    p2 = grid01.bar(ind, moderateMeans, width,bottom=mildMeans,color='#0000FF')
    p3 = grid01.bar(ind, severeMeans, width,bottom=[moderateMeans[i]+mildMeans[i] for i in range(N)],color='#FF8000')
    p4 = grid01.bar(ind, fatalMeans, width,bottom=[moderateMeans[i]+mildMeans[i]+severeMeans[i] for i in range(N)],color='#FF0000')

    plt.ylabel('Scores')
    plt.title('缺陷情况汇总图',fontsize=fontsize+5)
    plt.xticks(ind, state_list,fontsize=fontsize)
    plt.yticks(np.arange(0, sum([mildMeans[-1],moderateMeans[-1],severeMeans[-1],fatalMeans[-1]]), 10),fontsize=fontsize)
    plt.legend((p1[0], p2[0],p3[0],p4[0]), ('轻微', '一般','严重','致命'))
    #显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] =False
    for x1,y1 in enumerate(mildMeans):
        if y1==0:
            continue
        plt.text(x1,y1-0.5,"%s"%y1,va='center',fontsize=fontsize, wrap=True)
    for x2,y2 in enumerate(moderateMeans):
        y2_dire = mildMeans[x2]+y2
        if y2==0:
            continue
        plt.text(x2,y2_dire-0.5,"%s"%y2,va='center',fontsize=fontsize, wrap=True)
    for x3,y3 in enumerate(severeMeans):
        y3_dire=mildMeans[x3]+moderateMeans[x3]+y3
        if y3==0:
            continue
        plt.text(x3,y3_dire-0.5,"%s"%y3,va='center',fontsize=fontsize, wrap=True)
    for x4,y4 in enumerate(fatalMeans):
        y4_dire=mildMeans[x4]+moderateMeans[x4]+severeMeans[x4]+y4
        if y4==0:
            continue
        plt.text(x4,y4_dire-0.5,"%s"%y4,va='center',fontsize=fontsize, wrap=True)

    raw_labels = ['轻微', '一般','严重','致命','合计','占比']
    col_labels = state_list
    total = int((sum(mildMeans)+sum(moderateMeans)+sum(severeMeans)+sum(fatalMeans))/2)
    for i in range(len(state_list)):
        if i > 0 :
            table_vals[0].append(mildMeans[i])
            table_vals[1].append(moderateMeans[i])
            table_vals[2].append(severeMeans[i])
            table_vals[3].append(fatalMeans[i])
            table_vals[4].append(sum([mildMeans[i],moderateMeans[i],severeMeans[i]],fatalMeans[i]))
            table_vals[5].append('%.2f' % (table_vals[4][-1]/total * 100) +'%')
        else:
            table_vals = [[mildMeans[i]],[moderateMeans[i]],[severeMeans[i]],[fatalMeans[i]],[0],[0]]
            table_vals[4][0] = sum([mildMeans[i],moderateMeans[i],severeMeans[i]],fatalMeans[i])
            
            table_vals[5][0] = '%.2f' % (table_vals[4][0]/total * 100) +'%'
    col_labels.append('占比')
    for i in range(len(raw_labels)):
        if table_vals[i][-1] == '100.00%':
            table_vals[i].append('')
        else:
            table_vals[i].append('%.2f' % (table_vals[i][-1]/total *100) +'%')
    pprint(table_vals)
    
    plt.subplot(gs[15,0])
    plt.axis('off')
    table = plt.table(cellText=table_vals,colLabels=col_labels,rowLabels=raw_labels,loc='center',cellLoc='center',rowLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(fontsize)
    table.scale(1,1)
    plt.show()

def draw_everyday_bug_bar(everyday_bug_data,title='每天新增BUG数'):
    x_info,y_info = [],[]
    fontsize=12
    if '新增' in title:
        color = '#FF0000'
    if '关闭' in title:
        color = '#228B22'
    N = len(everyday_bug_data)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    for create_time in everyday_bug_data:
        x_info.append(create_time)
        y_info.append(everyday_bug_data[create_time])
    #比较大小，按日期顺序排序
    for i in range(len(x_info)):
        for j in range(len(x_info)-1):
            if isinstance(x_info[i],datetime.datetime) is False:
                x_info[i] = datetime.datetime.strptime(x_info[i],'%Y-%m-%d')
            if isinstance(x_info[j],datetime.datetime) is False:
                x_info[j] = datetime.datetime.strptime(x_info[j],'%Y-%m-%d')
            temp = x_info[i]
            if x_info[j].__gt__(temp):
                x_info[i] = x_info[j].strftime('%Y-%m-%d')
                x_info[j] = temp.strftime('%Y-%m-%d')
            else:
                x_info[i] = x_info[i].strftime('%Y-%m-%d')
                if isinstance(x_info[j],datetime.datetime):
                    x_info[j] = x_info[j].strftime('%Y-%m-%d')
    p1 = plt.bar(ind, y_info, width,color=color)

    plt.ylabel('')
    plt.title(title,fontsize=fontsize+5)
    plt.xticks(ind, x_info,rotation='vertical',fontsize=fontsize)
    plt.yticks(np.arange(0, max(y_info), 1),fontsize=fontsize)
    #plt.legend((p1[0]), ('轻微'))
    #显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] =False
    for x1,y1 in enumerate(y_info):
        if y1==0:
            continue
        plt.text(x1,y1-0.5,"%s"%y1,va='center',fontsize=fontsize, wrap=True)
    plt.show()

def draw_legacy_bug_bar(legacy_data,title='遗留BUG按严重程度分布'):
    fontsize = 13
    x_info,y_info = [],[]
    N = len(legacy_data)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    gs = gridspec.GridSpec(10,1) #表格和柱形图的分布
    raw_labels = ['占比', '值']
    table_vals = [[],[legacy_data[value] for value in legacy_data]]
    for create_time in legacy_data:
        x_info.append(create_time)
        y_info.append(legacy_data[create_time])
        temp = legacy_data[create_time]/legacy_data['合计'] *100
        table_vals[0].append('%.2f' % temp)
        table_vals[0][-1] += '%'
    grid01 = plt.subplot(gs[:7,0])  
    p1 = grid01.bar(ind, y_info, width)

    plt.ylabel('')
    plt.title(title,fontsize=fontsize+5)
    plt.xticks(ind, x_info,rotation='vertical',fontsize=fontsize)
    plt.yticks(np.arange(0, max(y_info), 3),fontsize=fontsize)
    #plt.legend((p1[0]), ('轻微'))
    #显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] =False
    for x1,y1 in enumerate(y_info):
        if y1==0:
            continue
        plt.text(x1,y1-0.5,"%s"%y1,va='center',fontsize=fontsize, wrap=True)
    print(table_vals)
    plt.subplot(gs[9,0])
    plt.axis('off')
    table = plt.table(cellText=table_vals,colLabels=x_info,rowLabels=raw_labels,loc='center',cellLoc='center',rowLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(fontsize)
    table.scale(1,1.5)

    plt.show()


def get_serveity_data(sht1_data,sht1_title,mildMeans,moderateMeans,severeMeans,fatalMeans,state_list):
    
    serveity = ["轻微","一般","严重","致命"]
    serveity_column,priority_column,state_column =0,0,0
    for i in range(len(sht1_title)):
        if '严重程度' in sht1_title[i]:
            serveity_column = i
        if '优先级' in sht1_title[i]:
            priority_column = i
        if '状态' in sht1_title[i]:
            state_column = i
    for i in range(len(sht1_data)):
        #获取严重程度按状态分 的数据
        if sht1_data[i][serveity_column] == serveity[0]: #轻微
            for j in range(len(state_list)):
                if sht1_data[i][state_column] == state_list[j]:
                    mildMeans[j] +=1
        elif sht1_data[i][serveity_column] == serveity[1]: #一般
            for j in range(len(state_list)):
                if sht1_data[i][state_column] == state_list[j]:
                    moderateMeans[j] +=1
        elif sht1_data[i][serveity_column] == serveity[2]: #严重
            for j in range(len(state_list)):
                if sht1_data[i][state_column] == state_list[j]:
                    severeMeans[j] +=1
        elif sht1_data[i][serveity_column] == serveity[3]: #致命
            for j in range(len(state_list)):
                if sht1_data[i][state_column] == state_list[j]:
                    fatalMeans [j] +=1
        else:
            pass
            #print(sht1_data[i][serveity_column])

    return mildMeans,moderateMeans,severeMeans,fatalMeans

def get_legacy_data(sht1_data,sht1_title,param='严重程度',legacy_data=dict()):
    #legacy_data = dict()
    legacy_state = ['待处理','修复中','重新打开','已解决']
    serveity_column,classification_column,module_column,state_column =0,0,0,0
    for i in range(len(sht1_title)):
        if '严重程度' in sht1_title[i]:
            serveity_column = i
        if sht1_title[i] in ['Bug类别','缺陷类型']:
            classification_column = i
        if sht1_title[i] in ['缺陷分类','分类']:
            module_column = i
        if '状态' in sht1_title[i]:
            state_column = i
    if  param=='严重程度':
        if '轻微' not in legacy_data:
            legacy_data = {"轻微":0,"一般":0,"严重":0,"致命":0}
        for i in range(len(sht1_data)):
            if sht1_data[i][state_column] in legacy_state:
                #获取严重程度按状态分 的数据
                if sht1_data[i][serveity_column] == "轻微": #轻微
                    legacy_data["轻微"] +=1
                elif sht1_data[i][serveity_column] == "一般": #一般
                    legacy_data["一般"] +=1
                elif sht1_data[i][serveity_column] == "严重": #严重
                    legacy_data["严重"] +=1
                elif sht1_data[i][serveity_column] == "致命": #致命
                    legacy_data["致命"] +=1
                else:
                    pass
        #legacy_data["合计"] = legacy_data["轻微"] + legacy_data["一般"] + legacy_data["严重"] +  legacy_data["致命"]
    if  param=='缺陷类型':
        for i in range(len(sht1_data)):
            
            if sht1_data[i][state_column] in legacy_state:
                classfiction_data = ["用户体验","功能问题","界面优化","兼容性问题","安全问题","性能问题","建议","需求变更","其他"]
                
                for k in classfiction_data:
                    if sht1_data[i][classification_column] and sht1_data[i][classification_column] in k:
                        sht1_data[i][classification_column] = k
                if sht1_data[i][classification_column] not in legacy_data:
                    legacy_data[sht1_data[i][classification_column]] =0
        print(legacy_data)
        for i in range(len(sht1_data)):
            if sht1_data[i][state_column] in legacy_state:
                legacy_data[sht1_data[i][classification_column]] += 1
                
    if  param=='缺陷分类':
        for i in range(len(sht1_data)):
            if sht1_data[i][state_column] in legacy_state and sht1_data[i][module_column] not in legacy_data:
                legacy_data[sht1_data[i][module_column]] = 0

        for i in range(len(sht1_data)):
            if sht1_data[i][state_column] in legacy_state:
                legacy_data[sht1_data[i][module_column]] += 1
                print(sht1_data[i][module_column])
                print(legacy_data[sht1_data[i][module_column]])

    
    if '合计' in legacy_data:
        legacy_data.pop('合计')
    legacy_data["合计"] = 0
    for value in legacy_data:
        if value =='合计':
            continue
        else:
            legacy_data["合计"] += legacy_data[value]
    
    
    print(legacy_data)
    return legacy_data

def get_everyday_bug_data(sht1_data,sht1_title,everyday_bug_data,param='创建'):
    time_column = 0
    for i in range(len(sht1_title)):
        if sht1_title[i] in ['完成时间','结束日期'] and param == '关闭':
            time_column = i
            break
        if sht1_title[i] in ['创建时间','创建于'] and param == '创建':
            time_column = i
            break
    for i in range(len(sht1_data)):
        if isinstance(sht1_data[i][time_column],datetime.datetime):
            temp_time = sht1_data[i][time_column].strftime('%Y-%m-%d')
            everyday_bug_data[temp_time] = 0
    
    for i in range(len(sht1_data)):
        if isinstance(sht1_data[i][time_column],datetime.datetime):
            temp_time = sht1_data[i][time_column].strftime('%Y-%m-%d')
            everyday_bug_data[temp_time] += 1
    return everyday_bug_data

def get_bar(src_file_list,param='严重程度'):
    """
    获取严重程度数据
    """
    everyday_bug_data,legacy_data = dict(),dict()
    legacy_data = dict()
    state_list = ['待处理', '已解决', '关闭', '已拒绝','重复BUG','合计']
    mildMeans,moderateMeans,severeMeans,fatalMeans = [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]

    for src_file in src_file_list:
        print(src_file)
        app = xw.App(visible=False, add_book=False)
        wb = app.books.open(src_file) # 打开Excel文件
        sht1 = wb.sheets[0]
        sht1_data = sht1.used_range.value
        sht1_title = sht1_data[0]

        if param=='严重程度':
            mildMeans,moderateMeans,severeMeans,fatalMeans = get_serveity_data(sht1_data,sht1_title,mildMeans,moderateMeans,severeMeans,fatalMeans,state_list)
        if param == '每天新增BUG数':
            everyday_bug_data = get_everyday_bug_data(sht1_data,sht1_title,everyday_bug_data)
        if param == '每天关闭BUG数':
            everyday_bug_data = get_everyday_bug_data(sht1_data,sht1_title,everyday_bug_data,param='关闭')
        if param == '遗留BUG按严重程度分布':
            legacy_data = get_legacy_data(sht1_data,sht1_title,param='严重程度',legacy_data=legacy_data)
        if param == '遗留BUG按缺陷类型分布':
            legacy_data = get_legacy_data(sht1_data,sht1_title,param='缺陷类型',legacy_data=legacy_data)
        if param == '遗留BUG按缺陷分类分布':
            legacy_data = get_legacy_data(sht1_data,sht1_title,param='缺陷分类',legacy_data=legacy_data)
        
        wb.save()
        wb.close()
        app.quit()

    if param=='严重程度':
        mildMeans[-1] = sum(mildMeans)
        moderateMeans[-1] = sum(moderateMeans)
        severeMeans[-1] = sum(severeMeans)
        fatalMeans[-1] = sum(fatalMeans)
        draw_serveity_bar(mildMeans,moderateMeans,severeMeans,fatalMeans,state_list)
        return '=== 按严重程度及状态汇总分布图 ==='
    if param in ['每天新增BUG数','每天关闭BUG数']:
        draw_everyday_bug_bar(everyday_bug_data,param)
        return '=== 开发过程中每天新增、解决、关闭缺陷分布图表 ==='
    if '遗留BUG' in param:
        draw_legacy_bug_bar(legacy_data,param)

    return '=== null ==='

if __name__ == "__main__":
    src_file_list = [
        '项目问题点.xls'
        
    ]
    #print(get_bar(src_file_list,param='严重程度'))
    #print(get_bar(src_file_list,param='每天新增BUG数'))
    #print(get_bar(src_file_list,param='每天关闭BUG数'))
    print(get_bar(src_file_list,param='遗留BUG按严重程度分布'))
    #print(get_bar(src_file_list,param='遗留BUG按缺陷类型分布'))
    #print(get_bar(src_file_list,param='遗留BUG按缺陷分类分布'))
    