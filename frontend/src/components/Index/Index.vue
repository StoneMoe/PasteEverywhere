<template>
    <div>
        <el-button icon="el-icon-info" size="small" class="help-button" circle @click="help()"></el-button>
        <div class="header-part">
            <div class="title">
                <span>{{ title }}</span>
            </div>
            <vue-typed-js class="desc" :strings="descriptions" :loop="true" :backDelay="5000">
                <span>
                    在这里
                    <span class="typing"></span>
                </span>
            </vue-typed-js>
        </div>
        <div class="upload-part">
            <div style="margin-bottom: 20px;">
                <el-button
                    :type="uploadType === 'string' ? 'primary' : ''"
                    icon="el-icon-edit"
                    circle
                    @click="uploadType = 'string'"
                ></el-button>
                <el-button
                    :type="uploadType === 'file' ? 'primary' : ''"
                    icon="el-icon-document"
                    circle
                    @click="uploadType = 'file'"
                ></el-button>
            </div>

            <div v-if="uploadType === 'file'">
                <el-upload
                    drag
                    :action="ApiUrls.IndexUpload"
                    :on-success="uploadFileOkHandler"
                    :on-error="uploadFileErrHandler"
                    :before-upload="beforeUploadFileHandler"
                >
                    <i class="el-icon-upload"></i>
                    <div class="el-upload__text">
                        将文件拖到此处，或
                        <em>点击上传</em>
                    </div>
                    <div class="el-upload__tip" slot="tip">不超过 10 MB 的任意文件</div>
                </el-upload>
            </div>
            <div v-else>
                <el-row type="flex" justify="center">
                    <el-col :span="8">
                        <el-input type="textarea" v-model="input" placeholder="要分享的内容"></el-input>
                    </el-col>
                </el-row>
                <el-row type="flex" justify="center" style="margin-top: 20px;">
                    <el-col :span="8">
                        <el-button
                            type="primary"
                            style="width:100%"
                            v-loading="uploadProcessing"
                            :disabled="input === '' || uploadProcessing"
                            @click="uploadText(input)"
                        >分享</el-button>
                    </el-col>
                </el-row>
            </div>
        </div>
    </div>
</template>

<script>
import { VueTypedJs } from "vue-typed-js";

export default {
    props: {
        title: String,
        desc: Array
    },
    components: {
        VueTypedJs
    },
    data() {
        return {
            descriptions: null,
            uploadType: "string",
            input: "",
            uploadProcessing: false
        };
    },
    methods: {
        help: function() {
            this.$alert(
                `<p>您可以分享无限长度的文字，或大小在<code> 10 MiB </code>以内的文件。</p><br>
                <p>每一个分享内容对应的临时链接，有效期为 15 分钟。</p>
                <p>链接有效期过后，对应的分享内容将永久删除且无法找回。</p><br>
                <p>在您使用该服务的过程中，不会产生任何能将分享内容与您的身份关联起来的日志。</p>
                <p>我们仅使用您的 IP 地址用于防滥用安全措施。</p><br>
                <p>本服务不兼容 GDPR 及与其相关的衍生法规，</p>
                <p>使用过程中请遵守您所在地以及本服务所处地区的法律法规。</p><br>
                <p>继续使用该服务视为您已知晓以上内容。</p>`,
                "说明",
                {
                    dangerouslyUseHTMLString: true
                }
            );
        },
        uploadText: function(str) {
            this.uploadProcessing = true;
            this.axios
                .post(this.ApiUrls.IndexUpload, {
                    text: str
                })
                .then(response => {
                    if (response.data.code !== 0) {
                        throw new Error(response.data.msg);
                    } else {
                        this.$alert(
                            `通过以下网址访问你所分享的文字，十五分钟内有效：\n ${
                                window.location.origin
                            }/s/${response.data.data}`,
                            "分享成功",
                            {
                                confirmButtonText: "好的",
                                callback: () => {
                                    this.input = "";
                                }
                            }
                        );
                    }
                })
                .catch(error => {
                    this.$message.error("分享失败: " + error.message);
                })
                .then(() => {
                    this.uploadProcessing = false;
                });
        },
        uploadFileOkHandler: function(response) {
            if (response.code !== 0) {
                this.$message.error(response.msg);
            } else {
                this.$alert(
                    `通过以下网址访问你所上传的文件，十五分钟内有效：\n ${
                        window.location.origin
                    }/s/${response.data}`,
                    "分享成功",
                    {
                        confirmButtonText: "好的",
                        callback: () => {
                            this.input = "";
                        }
                    }
                );
            }
        },
        uploadFileErrHandler: function(err, file) {
            this.$message.error(`文件 ${file.name} 上传失败`);
        },
        beforeUploadFileHandler: function(file) {
            const isLt2M = file.size / 1024 / 1024 < 10;
            if (!isLt2M) {
                this.$message.error("目前仅支持小于 10 MB 的文件");
            }
            return isLt2M;
        }
    },
    created() {
        this.descriptions = this.desc;
    }
};
</script>

<style>
.help-button {
    position: fixed;
    top: 5px;
    right: 5px;
}
.header-part {
    margin-top: 60px;
    text-align: center;
}
.title {
    font-size: 2em;
}
.title::first-letter {
    font-size: 1.3em;
    font-weight: bold;
}
.desc {
    display: block;
}
.upload-part {
    margin-top: 100px;
    margin-bottom: 70px;
    text-align: center;
}
</style>
