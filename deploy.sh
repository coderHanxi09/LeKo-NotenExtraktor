#!/bin/bash

# NotenExtraktor GitHub 部署脚本

echo "🚀 NotenExtraktor - GitHub 部署工具"
echo "=================================="
echo ""

# 检查是否安装了 git
if ! command -v git &> /dev/null; then
    echo "❌ 错误: 未安装 git"
    echo "请从 https://git-scm.com/ 安装 git"
    exit 1
fi

echo "📝 请输入您的 GitHub 用户名:"
read GITHUB_USERNAME

echo "📝 请输入仓库名（默认: LeKo-NotenExtraktor）:"
read REPO_NAME
REPO_NAME=${REPO_NAME:-LeKo-NotenExtraktor}

echo ""
echo "🔧 配置 Git..."
git config user.name "$GITHUB_USERNAME"
git config user.email "$GITHUB_USERNAME@users.noreply.github.com"

echo "📦 添加所有文件..."
git add .

echo "💾 创建提交..."
git commit -m "Initial NotenExtraktor Streamlit app deployment"

echo "🌿 重命名主分支..."
git branch -M main

echo "🔗 设置远程仓库..."
git remote remove origin 2>/dev/null || true
git remote add origin "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"

echo ""
echo "⚠️  下一步需要输入 GitHub 密码或 Personal Access Token"
echo "💡 提示: 建议使用 Personal Access Token 而非密码"
echo "   生成地址: https://github.com/settings/tokens"
echo ""
echo "🚀 推送到 GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 成功！"
    echo "📍 仓库地址: https://github.com/$GITHUB_USERNAME/$REPO_NAME"
    echo ""
    echo "🌐 现在可以部署到 Streamlit Cloud:"
    echo "   1. 访问 https://streamlit.io/cloud"
    echo "   2. 用 GitHub 登录"
    echo "   3. 点击 'New app'"
    echo "   4. 选择你的仓库: $GITHUB_USERNAME/$REPO_NAME"
    echo "   5. 点击 'Deploy'"
    echo ""
    echo "🎉 应用将在几分钟内上线！"
else
    echo ""
    echo "❌ 推送失败，请检查网络和 GitHub 凭证"
    exit 1
fi
