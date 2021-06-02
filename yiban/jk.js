banHtml = '<span style="background-color: #dc0505;font-size: 12px;color: #fff; padding: 0px 5px;margin:17px 0 0 5px;">被屏蔽</span>';
function getQues() {
    if (quesid == 0) {
        alert('获取问卷失败');
        return false;
    }
    $.ajax({
        'url': '/questionnaire/questionnaire/getQuiz/Quesid/' + quesid,
        'data': { 'order': 1 },
        'type': 'POST',
        'success': function (data) {
            data = eval('(' + data + ')');
            var showInfoHtml = '<a target="_blank" href="/questionnaire/index/showInfo/quesid/' + quesid + '" class="check">' + $('.article-title').html() + '</a>';
            if (data.code == 201) {
                beg = data.message;//开始页
                begHtml = '<div class="article-title clear">\
                        <p>'+ beg.title + '</p>\
                    </div>\
                    <div class="article-user-info nav_a_3">\
                        <span class="nav_a_2" style="float:left;"><em>(</em>'+ beg.startTime + '</span>\
                        <span class="span_5a" style="margin-top:30px;float:right;margin-right:10px;">本测试题共<span class="span_6" style="margin-right:0px;">&nbsp;'+ beg.quizNum + '&nbsp;</span>题</span>\
                    </div>\
                    <div>\
                    <div>\
                    </div>\
                    <div class="square_ya">\
                        <div class="square_ya1"> '+ beg.welcome + '</div>\
                    </div>\
                    <div class="button">\
                    <a href="javascript:void(0)" class="button_1 beg_btn"  style="margin-left:28%;" >开始答题</a>\
                    </div>';
                if (beg.showReport == '2') {
                    begHtml += '<div class="button" style="margin-top:50px">\
                        <a href="/questionnaire/index/report/quesid/'+ quesid + '" target="_blank" class="button_1" style="margin-left:28%;">查看报告</a>\
                        </div>';
                }
                begHtml += '</div>';
                $('#mainques').html(begHtml);
                if (beg.showPreview == '2' || beg.isAuthor == 1) {
                    $('.article-title').html(showInfoHtml);
                }
            }
            else if (data.code == 200) {//答题移步至新页面
                beg = data.message;
                begHtml = '<div class="article-title clear">\
                         <p>'+ beg.quesDetail.title + '</p>\
                     </div>\
                     <div class="article-user-info nav_a_3">\
                         <span class="nav_a_2" style="float:left;"><em>(</em>'+ beg.startTime + '</span>\
                         <span class="span_5a" style="margin-top:30px;float:right;margin-right:10px;">本测试题共<span class="span_6" style="margin-right:0px;">&nbsp;'+ beg.quizNum + '&nbsp;</span>题</span>\
                     </div>\
                     <div>\
                     <div>\
                     </div>\
                     <div class="square_ya">\
                         <div class="square_ya1"> '+ beg.quesDetail.welcome + '</div>\
                     </div>\
                     <div class="button">\
                     <a href="/questionnaire/index/nques/quesid/'+ quesid + '" class="button_1"  style="margin-left:28%;" >继续答题</a>\
                     </div>';
                if (beg.showReport == '2') {
                    begHtml += '<div class="button" style="margin-top:50px">\
                         <a href="/questionnaire/index/report/quesid/'+ quesid + '" target="_blank" class="button_1" style="margin-left:28%;">查看报告</a>\
                         </div>';
                }
                begHtml += '</div>';
                $('#mainques').html(begHtml);
                if (beg.showPreview == '2' || beg.isAuthor == 1) {
                    $('.article-title').html(showInfoHtml);
                }
            }
            else if (data.code == 202) {
                end = data.message;//查看报告
                endHtml = '<div class="article-title clear">\
                        <p>'+ end.title + '</p>\
                    </div>\
                    <div class="article-user-info nav_a_3">\
                        <span class="nav_a_2"><em>(</em>'+ end.startTime + '</span>\
                    </div>\
                    <div>\
                    <div>\
                        <span class="span_5a">本测试题共<span class="span_6">&nbsp;'+ end.quizNum + '&nbsp;</span>题</span>\
                    </div>\
                    <div class="square_yt">\
                        <span class="square_yt1">'+ end.finish + '</span>\
                   </div>';
                if (end.showReport == '1' || end.showReport == '2') {
                    endHtml += '<div class="button">\
                    <a href="/questionnaire/index/report/quesid/'+ quesid + '" target="_blank" class="button_1" style="margin-left:28%;">查看报告</a>\
                    </div>';
                }
                endHtml += '</div>';
                $('#mainques').html(endHtml);
                if (end.showPreview == '2' || end.isAuthor == 1 || (end.showPreview == '1' && end.hasFinish == 1)) {
                    $('.article-title').html(showInfoHtml);
                }
            } else if (data.code == 203) {
                end = data.message;//查看报告
                endHtml = '<div class="article-title clear">\
	                        <p>'+ end.title;
                if (end.isBan == '1') {
                    endHtml += banHtml;
                }
                endHtml += '</p>\
	                    </div>\
	                    <div class="article-user-info nav_a_3">\
	                        <span class="nav_a_2"><em>(</em>'+ end.startTime + '</span>\
	                    </div>\
	                    <div>\
	                    <div>\
	                        <span class="span_5a">本测试题共<span class="span_6">&nbsp;'+ end.quizNum + '&nbsp;</span>题</span>\
	                    </div>\
	                    <div class="square_yt">\
	                        <span class="square_yt1">';
                if (end.status == 3) {
                    endHtml += '问卷已回收';
                } else {
                    endHtml += end.finish;
                }
                endHtml += '</span></div><div class="button">\
	                    <a href="/questionnaire/index/report/quesid/'+ quesid + '" terget="_blank" class="button_1" style="margin-left:28%;">查看报告</a>\
	                    </div>';
                endHtml += '</div>';
                $('#mainques').html(endHtml);
                if (end.showPreview == '2' || end.isAuthor == 1 || (end.showPreview == '1' && end.hasFinish == 1)) {
                    $('.article-title').html(showInfoHtml);
                }
            } else if (data.code == 205) {//问卷已结束
                var _html = ' <div><span class="span_5a">本测试题共<span class="span_6">&nbsp;' + data.message.quizNum + '&nbsp;</span>题</span>\
                    </div><div class="square_yt">\
                    <span class="square_yt1">问卷已回收</span></div>';
                if ((data.message.showReport == '1' && data.message.hasFinish == 1) || data.message.showReport == '2') {
                    _html += '<div class="button">\
		                    <a href="/questionnaire/index/report/quesid/'+ quesid + '" target="_blank" class="button_1" style="margin-left:28%;">查看报告</a>\
		                    </div>';
                }
                $('#mainques').append(_html);
                if (data.message.showPreview == '2' || data.message.isAuthor == 1 || (data.message.showPreview == '1' && data.message.hasFinish == 1)) {
                    $('.article-title').html(showInfoHtml);
                }
                return false;
            } else {
                alert(data.message);
                return false;
            }
        }
    })

}


$('.beg_btn').live('click', function () {//开始问卷
    if (quesid == 0) {
        alert('获取问卷失败');
        return false;
    }
    $.ajax({
        'url': '/questionnaire/questionnaire/startQuiz/Quesid/' + quesid,
        'data': { 'answer': 'nnnn' },
        'type': 'POST',
        'success': function (data) {
            data = eval('(' + data + ')');

            if (data.code == 200) {
                location.href = '/questionnaire/index/nques/quesid/' + quesid;
                getQues();
                return true;
            }
            else {
                alert(data.message);
                return false;
            }
        }
    })
});
$('.last_btn').live('click', function () {//上一题
    if (quesid == 0) {
        alert('获取问卷失败');
        return false;
    }
    $.ajax({
        'url': '/questionnaire/questionnaire/prevQuiz/Quesid/' + quesid,
        'data': { 'answer': 'nnnn' },
        'type': 'POST',
        'success': function (data) {
            data = eval('(' + data + ')');
            if (data.code == 200) {
                getQues();
                return true;
            }
            else {
                alert(data.message);
                return false;
            }
        }
    })
});
$('.next_btn').live('click', function () {//下一题
    if (quesid == 0) {
        alert('获取问卷失败');
        return false;
    }
    answer = false;
    answermore = false;
    quiztype = $(this).data('quiztype');
    answerRes = Quiz.Q(quiztype).getAnswer();
    if (!answerRes) {
        return false;
    }
    $.ajax({
        'url': '/questionnaire/questionnaire/answerQuiz/Quesid/' + quesid,
        'data': { 'answer': answerRes.answer, 'answermore': answerRes.answermore },
        'type': 'POST',
        'success': function (data) {
            data = eval('(' + data + ')');
            if (data.code == 200) {
                if (data.data == 'last') {//最后一个回答问卷的人
                    alert('感谢您的参与，问卷已达到有效数量，将回收下线。');
                    location.href = '/questionnaire/index/index';
                    return false;
                }
                getQues();
                return true;
            }
            else {
                alert(data.message);
                return false;
            }
        }
    })
})


